import tkinter
import customtkinter  # <- import the CustomTkinter module
from functions import create_task, delete_task
import os


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()  # create the Tk window like you normally do
root.geometry("800x550")
root.title("Scheduler")

tabview = customtkinter.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)

tabview.add("create")  # add tab at the end
tabview.add("edit or remove")  # add tab at the end
tabview.set("create")  # set currently visible tab

def checkboxes_clicked():
    for idx, day in enumerate(days):
        state = day_vars[idx].get()
        if state == 1:
            return True
        
def delete_button_function():
    delete_task(optionmenu.get())
    with open('task_names.log', "r+" ) as file:
        lines = file.readlines()
        file.seek(0)
        idx = lines.index(optionmenu.get()+"\n")
        lines.pop( idx )
        file.truncate()
        file.writelines( lines )

def button_function():
    if hours_entry.get() == "" or minutes_entry.get() == "" or seconds_entry.get() == "" or ampm_entry.get() == "":
        print("Please input valid information")
    else:
        if checkboxes_clicked():
            print("button pressed")
            WeeklySchedule = 0
            for idx, day in enumerate(days):
                state = day_vars[idx].get()
                if state == True:
                    WeeklySchedule += days_decimal_value[idx]
                    print(day)
                print(f"{day} checkbox is {state}")
            print(WeeklySchedule)
            print(link_entry.get())
            print(hours_entry.get()+':'+minutes_entry.get()+':'+seconds_entry.get()+ampm_entry.get())
            print(ampm_entry.get())
            wake = wake_checkbox.get()
            hours = hours_entry.get()
            minutes = minutes_entry.get()
            seconds = seconds_entry.get()
            if ampm_entry.get() == 0:
                ampm = "AM"
            else:
                ampm = ampm_entry.get().upper()
            myBat = open(r'open_Meeting.bat', 'w+')
            myBat.write('start '+link_entry.get())
            myBat.close()
            # os.chdir(os.getcwd())
            # os.startfile("open_Meeting.bat")
            path = os.getcwd() + "/" + "open_Meeting.bat"
            name = name_entry.get()

            with open('task_names.log', 'w+') as file:
                file.write(name_entry.get() + " - enabled")
                file.close()

            create_task(name, path, WeeklySchedule, hours, minutes, seconds, ampm, wake)

        else:
            print("please choose at least one of the following days")

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

def checkbox_event():
    # Handle checkbox events if needed
    for idx, day in enumerate(days):
        state = day_vars[idx].get()
        print(f"{day} checkbox is {state}")
    state = wake_checkbox.get()
    print(f"Wake checkbox is {state}")

frame = customtkinter.CTkFrame(master=tabview.tab("create"))
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Schedule")
label.pack(pady=12, padx=10)

entry_frame1 = customtkinter.CTkFrame(master=frame)
entry_frame1.pack(pady=12, padx=10)

name_entry = customtkinter.CTkEntry(master=entry_frame1, placeholder_text="Name of task")
name_entry.pack(side='left',pady=1, padx=1)

link_entry = customtkinter.CTkEntry(master=entry_frame1, placeholder_text="link")
link_entry.pack(side='right',pady=1, padx=1)

entry_frame = customtkinter.CTkFrame(master=frame)
entry_frame.pack(pady=12, padx=10)

entry_width = 28
default_value = 00

hours_entry = customtkinter.CTkEntry(master=entry_frame, placeholder_text="00", width=entry_width)
# hours_entry.insert(0, default_value) # Set the default value
hours_entry.pack(side='left',padx=5, pady=5)

label = customtkinter.CTkLabel(master=entry_frame, text=":")
label.pack(side='left',pady=1, padx=1)

minutes_entry = customtkinter.CTkEntry(master=entry_frame, placeholder_text="00", width=entry_width)
# minutes_entry.insert(0, default_value)  # Set the default value
minutes_entry.pack(side='left',pady=5, padx=5)

label = customtkinter.CTkLabel(master=entry_frame, text=":")
label.pack(side='left',pady=1, padx=1)

seconds_entry = customtkinter.CTkEntry(master=entry_frame, placeholder_text="00", width=entry_width)
# seconds_entry.insert(0, default_value)  # Set the default value
seconds_entry.pack(side='left',pady=5, padx=5,)

# ampm_entry = customtkinter.CTkEntry(master=entry_frame, placeholder_text="----", width=entry_width+5)
# ampm_entry.insert(0, "AM")  # Set the default value
# ampm_entry.pack(side='left',pady=5, padx=5)

ampm_entry = customtkinter.StringVar(value="AM")
ampm_entry = customtkinter.CTkOptionMenu(entry_frame, values=["AM", "PM"], command=optionmenu_callback, variable=ampm_entry, width=entry_width)
ampm_entry.pack(side='left',pady=5, padx=5)

button = customtkinter.CTkButton(master=frame, text="create", corner_radius=10, command=button_function)
button.pack(pady=12, padx=10)

frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=10, padx=10, fill="both", expand=True)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_decimal_value = [2, 4, 8, 16, 32, 64, 1]
day_vars = []
checkboxes = {}

num_cols = 2
for idx, day in enumerate(days):
    var = customtkinter.IntVar(value=0)
    day_vars.append(var)
    row = idx % (len(days) // num_cols)
    col = idx // (len(days) // num_cols)
    checkbox = customtkinter.CTkCheckBox(frame2, text=day, command=checkbox_event, variable=day_vars[idx], onvalue=1, offvalue=0)
    checkbox.grid(row=row, column=col, padx=10, pady=12)
    checkboxes[day] = checkbox  # Store checkbox in dictionary with day as key

check_var = customtkinter.IntVar(value=0)
wake_checkbox = customtkinter.CTkCheckBox(frame2, text="Wake computer to run task?", command=checkbox_event, variable=check_var, onvalue=1, offvalue=0)
wake_checkbox.grid(row=0, column=3, padx=10, pady=12)

frame = customtkinter.CTkFrame(master=tabview.tab("edit or remove"))
frame.pack(side='left', pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Your Custom Tasks")
label.pack(pady=12, padx=10)

textbox = customtkinter.CTkTextbox(master=frame)
textbox.pack(pady=12, padx=10)
with open('task_names.log', 'r') as file:
    textbox.insert("0.0", file.read())
    file.close()
textbox.configure(state="disabled")  # configure textbox to be read-only

frame = customtkinter.CTkFrame(master=tabview.tab("edit or remove"))
frame.pack(side='right', pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Options")
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Delete", corner_radius=10, command=delete_button_function)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Disable", corner_radius=10, command=delete_button_function)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Enable", corner_radius=10, command=delete_button_function)
button.pack(pady=12, padx=10)


with open('task_names.log', 'r') as file:
    names = file.readlines()
    names = [i.strip() for i in names]
    names = [i.replace(i[i.find('-')-1:],'') for i in names]
    print(names)
    file.close()


optionmenu_var = customtkinter.StringVar(value=names[0])
optionmenu = customtkinter.CTkOptionMenu(frame, values=names, command=optionmenu_callback, variable=optionmenu_var)
optionmenu.pack(pady=12, padx=10)


root.mainloop()

#-after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
