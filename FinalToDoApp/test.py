from tkinter.ttk import *
from tkinter import messagebox
from tkinter.scrolledtext import *
from tkcalendar import DateEntry
import json
from tkinter import *

tk = Tk()
tk.geometry("800x600")
tk.config(bg="black")
tk.title("Task Organiser")
all_tasks_to_write = []


# open and edit external files
def get_all_tasks_from_file():
    with open("db.txt", "r") as file:
        try:
            existing_tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_tasks = []
    all_tasks_to_write.extend(existing_tasks)
    return all_tasks_to_write


def write_tasks_to_file():
    with open("db.txt", "w") as file:
        # deletes file from start
        # file.seek(0)
        # file.truncate()
        # save complicated expressions as json format
        json.dump(all_tasks_to_write, file)


def clear_view():
    for s in tk.grid_slaves():
        s.destroy()
    # grids_slaves gives a list of the elements in the grid


def create_task(**kwargs):
    # creates dictionary of named arguments
    all_tasks_to_write.append(kwargs)
    write_tasks_to_file()


def render_list_task_view():
    clear_view()
    dropdown = Combobox(tk, width=130)
    dropdown['values'] = all_tasks_to_write
    dropdown.grid(row=0, column=0, columnspan=3)
    Button(tk, text="Edit", width=10, command=lambda: render_edit_task(eval(dropdown.get()), False), bg="yellow", fg="black",
           font="16").grid(row=1, column=0, pady="400")
    Button(tk, text="Delete", width=10, command=lambda: delete_task(eval(dropdown.get())), bg="red", fg="black",
           font="16").grid(row=1, column=1, pady="400")
    Button(tk, text="Cancel", width=10, bg="Gray", fg="black",
           font="16", command=lambda: render_main_view()).grid(row=1, column=2, pady="400")


def delete_task(to_delete):
    all_tasks_to_write.remove(to_delete)
    write_tasks_to_file()
    render_list_task_view()


def render_edit_task(to_edit, is_newtask):
    clear_view()
    Label(tk, text="Enter your task name:").grid(row=0, column=0, padx=10, pady=10)
    task_name = Entry(tk)
    task_name.insert(0, to_edit['name'])
    task_name.grid(row=0, column=1, padx=20, pady=10)
    Label(tk, text="Due Date:").grid(row=1, column=0, padx=10, pady=10)
    date = DateEntry(tk)
    date.delete(0, END)
    date.insert(0, to_edit['date'])
    date.grid(row=1, column=1, padx=20, pady=20)
    Label(tk, text="description").grid(row=2, column=0, padx=10, pady=10)
    description = ScrolledText(tk, width=30, height=10)
    description.insert(INSERT, to_edit['description'])
    description.insert(END, "")
    description.grid(row=2, column=1)
    Label(tk, text="Select Priority").grid(row=3, column=0, padx=10, pady=10)
    selected = IntVar()
    selected.set(to_edit['priority'])
    raid1 = Radiobutton(tk, text="Low", value=1, variable=selected)
    raid2 = Radiobutton(tk, text="Medium", value=2, variable=selected)
    raid3 = Radiobutton(tk, text="High", value=3, variable=selected)
    raid1.grid(row=3, column=1)
    raid2.grid(row=3, column=2)
    raid3.grid(row=3, column=3, padx=100)
    Label(tk, text="Check if completed").grid(row=4, column=0, padx=10, pady=10)
    completed = BooleanVar()
    completed.set(to_edit["iscompleted"])
    Checkbutton(tk, text="Completed", variable=completed).grid(row=4, column=1)
    # Extract variables into named arguments
    if is_newtask:
        Button(tk, text="Create Task", bg="Green", fg="white", font="16",
               command=lambda: eddit_trigger(to_edit, name=task_name.get(), date=date.get(),
                                             description=description.get("1.0", END),
                                             priority=completed.get(),
                                             iscompleted=completed.get())).grid(
            row=5,
            column=1,
            pady=150)
    else:
        Button(tk, text="Edit", bg="Orange", fg="white", font="16",
               command=lambda: eddit_trigger(to_edit, name=task_name.get(), date=date.get(),
                                             description=description.get("1.0", END),
                                             priority=completed.get(),
                                             iscompleted=completed.get())).grid(
            row=5,
            column=1,
            pady=150)
    Button(tk, text="Cancel", bg="Gray", fg="white", font="16",
           command=lambda: render_main_view()).grid(row=5, column=2, pady=150)


def eddit_trigger(to_edit, **kwargs):
    m = messagebox.askquestion("Edit", "Are you sure you want to edit?")
    if m == "yes":
        create_task(**kwargs)
        delete_task(to_edit)


def render_create_task_view():
    new_task = {'name': '', 'date': '', 'description': '', 'priority': 0, 'iscompleted': 'False'}
    is_newtask = True
    render_edit_task(new_task, is_newtask)


def render_main_view():
    clear_view()
    Button(tk, text="List Tasks", bg="blue", fg="white", font="16", command=render_list_task_view).grid(row=0, column=0,
                                                                                                        padx=150,
                                                                                                        pady=100)
    Button(tk, text="Create Task", bg="green", fg="white", font="16", command=render_create_task_view).grid(
        row=0,
        column=1,
        padx=100,
        pady=100)


render_main_view()
all_tasks_to_write = get_all_tasks_from_file()
write_tasks_to_file()
tk.mainloop()
