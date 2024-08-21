import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from datetime import datetime
import time
import threading
from plyer import notification

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("430x430")
        self.title("Todo List App")
        self.configure(bg="#212121")

        self.create_widgets()
    
    def create_widgets(self):
        # Input Entry
        self.task_input = tk.Entry(self, width=30, bg="#303030", fg="#ffffff", insertbackground="#ffffff")
        self.task_input.pack(pady=10)

        # Add Task Button
        self.add_task_btn = tk.Button(self, text="Add Task", bg="#1DA756", fg="#212121", command=self.add_task)
        self.add_task_btn.pack(pady=5)

        # Task List
        self.task_list = tk.Listbox(self, selectmode=tk.SINGLE, bg="#303030", fg="#ffffff", selectbackground="#1DA756", selectforeground="#212121")
        self.task_list.pack(pady=5, fill=tk.BOTH, expand=True)

        # Button Frame
        self.btn_frame = tk.Frame(self, bg="#212121")
        self.btn_frame.pack(pady=5)

        # Edit Task Button
        self.edit_task_btn = tk.Button(self.btn_frame, text="Edit Task", bg="#1DA756", fg="#212121", command=self.edit_task)
        self.edit_task_btn.grid(row=0, column=0, padx=5)

        # Delete Task Button
        self.delete_task_btn = tk.Button(self.btn_frame, text="Delete Task", bg="#FF4D4D", fg="#ffffff", command=self.delete_task)
        self.delete_task_btn.grid(row=0, column=1, padx=5)

        # Save Task Button
        self.save_task_btn = tk.Button(self.btn_frame, text="Save Task", bg="#1DA756", fg="#212121", command=self.save_task)
        self.save_task_btn.grid(row=0, column=2, padx=5)

        # Load Task Button
        self.load_task_btn = tk.Button(self.btn_frame, text="Load Task", bg="#1DA756", fg="#212121", command=self.load_task)
        self.load_task_btn.grid(row=0, column=3, padx=5)

        # Mark as Complete Button
        self.mark_complete_btn = tk.Button(self.btn_frame, text="Mark as Complete", bg="#1DA756", fg="#212121", command=self.mark_as_complete)
        self.mark_complete_btn.grid(row=0, column=4, padx=5)

    def add_task(self):
        task_name = self.task_input.get().strip()
        if not task_name:
            messagebox.showwarning("Warning", "Task name cannot be empty")
            return

        due_date = simpledialog.askstring("Input", "Enter due date (YYYY-MM-DD) or leave empty:")
        task_entry = task_name
        if due_date:
            task_entry += f" [Due: {due_date}]"

        reminder = messagebox.askyesno("Reminder", "Do you want to set a reminder?")
        if reminder:
            reminder_time = simpledialog.askstring("Input", "Enter reminder date and time (YYYY-MM-DD HH:MM):")
            if reminder_time:
                self.schedule_reminder(task_name, reminder_time)
        
        self.task_list.insert(tk.END, task_entry)
        self.task_input.delete(0, tk.END)

    def edit_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            current_task = self.task_list.get(task_index)
            task_name = current_task.split(' [Due:')[0]
            self.task_input.delete(0, tk.END)
            self.task_input.insert(0, task_name)
            self.task_list.delete(task_index)
        else:
            messagebox.showwarning("Warning", "Select a task to edit")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Select a task to delete")

    def save_task(self):
        tasks = self.task_list.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Info", "Tasks saved successfully")

    def load_task(self):
        self.task_list.delete(0, tk.END)
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    self.task_list.insert(tk.END, task.strip())
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No saved tasks found")

    def mark_as_complete(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            current_task = self.task_list.get(task_index)
            if not current_task.endswith("✔"):
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, current_task + " ✔")
        else:
            messagebox.showwarning("Warning", "Select a task to mark as complete")

    def schedule_reminder(self, task_name, reminder_time_str):
        def reminder_thread(task_name, reminder_time_str):
            reminder_time = datetime.strptime(reminder_time_str, '%Y-%m-%d %H:%M')
            while datetime.now() < reminder_time:
                time.sleep(10)
            notification.notify(
                title="Reminder",
                message=f"Time to: {task_name}",
                app_name="Todo List App"
            )

        threading.Thread(target=reminder_thread, args=(task_name, reminder_time_str), daemon=True).start()

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
