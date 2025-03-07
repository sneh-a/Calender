import calendar
import tkinter as tk
from tkinter import ttk

def show_calendar():
    try:
        yy = int(year_entry.get())
        mm = int(month_entry.get())
        cal_text.set(calendar.month(yy, mm))
    except ValueError:
        cal_text.set("Invalid Input. Enter valid Year and Month.")

# Create main window
root = tk.Tk()
root.title("Calendar Viewer")
root.geometry("400x400")

# Title Label
tk.Label(root, text="Calendar Viewer", font=("Arial", 16, "bold")).pack(pady=10)

# Year Input
tk.Label(root, text="Enter Year:", font=("Arial", 12)).pack()
year_entry = tk.Entry(root, font=("Arial", 12))
year_entry.pack(pady=5)

# Month Input
tk.Label(root, text="Enter Month (1-12):", font=("Arial", 12)).pack()
month_entry = tk.Entry(root, font=("Arial", 12))
month_entry.pack(pady=5)

# Button
tk.Button(root, text="Show Calendar", command=show_calendar, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Display Calendar
cal_text = tk.StringVar()
cal_label = tk.Label(root, textvariable=cal_text, font=("Courier", 12), justify="left", bg="white", relief="solid", width=30, height=10)
cal_label.pack(pady=10)

root.mainloop()
