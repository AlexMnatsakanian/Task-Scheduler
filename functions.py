import datetime
import win32com.client
import os
def convert_standard_to_military(hours, minutes, seconds, am_pm):
    # Convert to 24-hour format
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    am_pm = am_pm.upper()
    if am_pm == 'PM' and hours < 12:
        hours += 12  # Add 12 hours to convert from PM to 24-hour format (except for 12 PM)
    elif am_pm == 'AM' and hours == 12:
        hours = 0  # Handle 12 AM (midnight)
    return hours, minutes, seconds

def create_task(name, path, weekly_schedule, hr, min, sec, ampm, wake):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Set the start time for the task
    start_time = datetime.datetime.now() + datetime.timedelta(minutes=1)

    # Create a trigger for specific days of the week and time of day
    TASK_TRIGGER_WEEKLY = 3
    trigger = task_def.Triggers.Create(TASK_TRIGGER_WEEKLY)
    trigger.DaysOfWeek = weekly_schedule  # 0x1C represents Monday, Tuesday, and Wednesday

    # Set the time when the task should run on those days
    military_time = convert_standard_to_military(hr, min, sec, ampm)
    trigger.StartBoundary = start_time.replace(hour=military_time[0], minute=military_time[1], second=military_time[2]).isoformat()  # Set to 10:00 AM

    # Create action to execute a batch file
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'TRIGGER BATCH'
    action.Path = 'cmd.exe'
    action.Arguments = '/c start "" ' + path

    # Set parameters for the task
    task_def.RegistrationInfo.Description = 'Test Task'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False
    task_def.Settings.WakeToRun = wake

    # Register the task
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    root_folder.RegisterTaskDefinition(
        name,  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        '',  # No user
        '',  # No password
        TASK_LOGON_NONE
    )
path = os.getcwd()+"/"+"open_Meeting.bat"
create_task("taskkkerrrr", path, 127, 10, 25, 00, 'pm', True)

def delete_task(name):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')

    task_name = name

    try:
        # Get the task by name
        task = root_folder.GetTask(task_name)

        # Delete the task
        root_folder.DeleteTask(task.Name, 0)  # 0 means delete the task without confirmation

        print(f"Task '{task_name}' deleted successfully.")

    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")
