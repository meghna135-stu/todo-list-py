import tkinter as tk
import json
from tkinter import messagebox

# Load tasks from file
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

# Save tasks
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Refresh UI
def refresh_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

# Add Task
def add_task():
    task_name = task_entry.get()

    if task_name:
        # Prevent duplicate tasks
        if any(task["task"] == task_name for task in tasks):
            print("Task already exists")
            return

        tasks.append({"task": task_name, "done": False})
        save_tasks()
        refresh_listbox()
        task_entry.delete(0, tk.END)

# Delete Task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        save_tasks()
        refresh_listbox()

# Mark Complete
def mark_complete():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        save_tasks()
        refresh_listbox()

# Clear All Tasks
def clear_all():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
    if confirm:
        tasks.clear()
        save_tasks()
        refresh_listbox()
        messagebox.showinfo("Done", "All tasks cleared!")
# ---------------- UI ---------------- #

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Title
title = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input box
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
task_entry.focus()

# Add button
add_button = tk.Button(root, text="Add Task", width=20, bg="lightblue", command=add_task)
add_button.pack()

# Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=40, height=12, yscrollcommand=scrollbar.set)
task_listbox.pack(side=tk.LEFT)

scrollbar.config(command=task_listbox.yview)

# Buttons
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Complete", width=20, command=mark_complete)
complete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", width=20, command=clear_all)
clear_button.pack(pady=5)

# Load existing tasks
refresh_listbox()

# Run app
root.mainloop()