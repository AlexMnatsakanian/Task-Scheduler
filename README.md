# Scheduler Application

## Description
This Python application allows users to schedule tasks on their Windows system using a graphical user interface (GUI) built with Tkinter. Users can create, edit, remove, enable, and disable tasks easily through the interface.

## Prerequisites
- Python 3.x
- `tkinter` library
- `win32com.client` library

## Installation
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install required libraries:
   ```
   pip install tk
   pip install pywin32
   ```
   
## Usage
1. Run `main.py` to launch the application.
2. Use the GUI to create, edit, remove, enable, or disable tasks.
3. Follow the instructions provided in the application.

## Files
- `main.py`: Contains the main code for the scheduler application.
- `functions.py`: Contains functions for creating and deleting tasks using Windows Task Scheduler.

## Features
- Create tasks with specific names, links, schedules, and wake options.
- View existing tasks and their details.
- Delete tasks by selecting them from a dropdown menu.
- Enable or disable tasks as needed. **(In progress)**

## How to Use
1. Launch the application by running `main.py`.
2. Fill in the required information to create a new task:
   - Name of the task
   - Link to be opened
   - Schedule: Days of the week and time
   - Options: Whether to wake the computer to run the task
3. Click the "Create" button to create the task.
4. View existing tasks and their details in the "Edit or Remove" tab.
5. Select a task from the dropdown menu to delete, enable, or disable it.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
