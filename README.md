## **"Feature-Rich Todo List App with Reminders and Notifications Using Tkinter"**

**Description:**

This is a feature-rich Todo List application developed using Python's Tkinter library. It provides an intuitive interface for managing tasks with features such as adding, editing, deleting, saving, loading tasks, and setting reminders. The app also supports task completion marking and user notifications for reminders using the Plyer library.

**Features:**

- **Task Management:**
  - Add tasks with optional due dates and reminders.
  - Edit or delete existing tasks.
  - Mark tasks as complete with a visual indicator.

- **File Operations:**
  - Save tasks to a file.
  - Load tasks from a file.

- **Reminders:**
  - Schedule reminders with date and time notifications.
  - Notifications are triggered using the Plyer library.

- **User Interface:**
  - A clean, user-friendly interface with custom colors and layouts.
  - Input fields for task details and buttons for various operations.

**Technologies Used:**

- **Python:** Core programming language used for developing the application.
- **Tkinter:** GUI toolkit for creating the application window and interface elements.
- **Plyer:** Library for desktop notifications.
- **Threading:** Used for managing reminder notifications without blocking the main application thread.
- **File I/O:** For saving and loading tasks to/from a text file.

**Code Overview:**

The application is structured into a `TodoListApp` class which inherits from `tk.Tk`, encompassing methods for:
- **Creating UI Components:** Including task input fields, buttons, and listbox.
- **Task Operations:** Such as adding, editing, deleting, and saving tasks.
- **Reminder Management:** Scheduling notifications using threading and the Plyer library.
- **File Handling:** For saving and loading tasks from a text file.

**Installation and Usage:**

1. **Install Dependencies:**
   - Ensure you have `Tkinter` and `Plyer` installed. Install Plyer using:
     ```bash
     pip install plyer
     ```

2. **Run the Application:**
   - Execute the script:
     ```bash
     python todo_list_app.py
     ```

3. **Using the App:**
   - Add tasks by typing in the input field and pressing "Add Task."
   - Set reminders when adding tasks.
   - Edit or delete tasks using the respective buttons.
   - Save and load tasks with file operations.
   - Mark tasks as complete by selecting and using the "Mark as Complete" button.

**Contributing:**

Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!

**License:**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Skills Used:**
- **Python Programming:** Core language for development.
- **Tkinter:** GUI creation and management.
- **Plyer:** Notifications and system alerts.
- **Threading:** Background task management.
- **File I/O:** Data storage and retrieval.
- **UI/UX Design:** Designing user interfaces with a focus on user experience.
