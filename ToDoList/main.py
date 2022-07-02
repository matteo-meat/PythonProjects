import tkinter.messagebox
from tkinter import *


def add_task(entry: Entry, listbox: Listbox):

    new_task = entry.get()

    if new_task == "":
        tkinter.messagebox.showerror("Error", "Please fill the entry box!")
    else:
        new_task += "\n"
        with open("tasks.txt", "r+") as my_file:
            content = my_file.readlines()
            if new_task in content:
                tkinter.messagebox.showerror("Error", "Already in list!")
            else:
                my_file.write(new_task)
                listbox.insert(END, new_task)
                new_task_entry.delete(0, "end")


def delete_task(listbox: Listbox):

    with open("tasks.txt", "r") as my_file:
        lines = my_file.readlines()

    to_delete = listbox.get(listbox.curselection())
    deleted = False

    with open("tasks.txt", "w") as my_file:
        for line in lines:
            if line != to_delete:
                my_file.write(line)
            else:
                deleted = True

    if deleted:
        lines.remove(to_delete)

    listbox.delete(ACTIVE)
    delete_btn.configure(state="disabled")


def callback(event):
    if len(tasks.curselection()) != 0:
        delete_btn.configure(state="active")
    else:
        delete_btn.configure(state="disabled")


# Initialize the GUI window
root = Tk()
root.title("Matteo's To-Do List")
root.geometry("300x400")
root.resizable(1, 1)
root.config(bg="PaleVioletRed")

# Heading Label
Label(root, text="Matteo's Python To-Do List", bg="PaleVioletRed", font=("Comic Sans MS", 15), wraplength=300).place(x=35, y=0)

# Listbox with all the tasks with a Scrollbar
tasks = Listbox(root, selectbackground="Gold", bg="Silver", font=("Helvetica", 12), height=12, width=25)
tasks.bind("<<ListboxSelect>>", callback)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=220)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=35, y=50)

try:
    with open("tasks.txt", "r+") as tasks_list:
        for task in tasks_list:
            tasks.insert(END, task)
except FileNotFoundError:
    with open("tasks.txt", "a+") as tasks_list:
        for task in tasks_list:
            tasks.insert(END, task)

# Creating the Entry widget where the user can enter a new item
new_task_entry = Entry(root, width=27)
new_task_entry.place(x=35, y=310)

# Creating the Buttons
add_btn = Button(root, text="Add Item", bg="Azure", width=10, font=("Helvetica", 12), command=lambda: add_task(new_task_entry, tasks))
add_btn.place(x=45, y=350)

delete_btn = Button(root, text="Delete Item", bg="Azure", width=10, font=("Helvetica", 12), command=lambda: delete_task(tasks))
delete_btn.place(x=150, y=350)
delete_btn.configure(state="disabled")

# Finalizing the window
root.update()
root.mainloop()