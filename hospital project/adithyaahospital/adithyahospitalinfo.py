import tkinter as tk
from tkinter import messagebox, PhotoImage
import subprocess

# Create the tkinter window
root = tk.Tk()
root.title("ADITHYA HOSPITAL DOCTOR DETAILS")

# Set background image
bg_image = PhotoImage(file=r"C:\Users\vasanth kumar\Downloads\422212 (1).png")  # replace 'background.png' with your image file
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to open appointment page
def open_appointment_page():
    subprocess.run(["python", "main.py"])

# Function to open doctor page
def open_doctor_page():
    subprocess.run(["python", "doctor.py"])

# Function to open insurance page
def insurance_page():
    subprocess.run(["python", "insurance.py"])

def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to exit the program?"):
        root.destroy()

# Create option frame
option_frame= tk.Frame(root, bg="GRAY")

# Add logo to the option frame
logo_image = PhotoImage(file=r"C:\Users\vasanth kumar\Downloads\2-.png")
resized_logo = logo_image.subsample(4, 3)  # Adjust size as needed
logo_label = tk.Label(option_frame, image=resized_logo)
logo_label.pack(pady=20)  # Add padding if needed


# Create menu button within the option frame
menu_page = tk.Button(option_frame, text='MENU', font=("bold", 15), fg="black", bd=0)
menu_page.pack(pady=10)  # Add padding if needed

# Create appointments button within the option frame
Appointments_page = tk.Button(option_frame, text='APPOINTMENT', font=("bold", 15), fg="black", bd=0, command=open_appointment_page)
Appointments_page.pack(pady=10)  # Add padding if needed

# Create doctor details button within the option frame
DOCTOR_DETAILS = tk.Button(option_frame, text='DOCTOR DETAILS', font=("bold", 15), fg="black", bd=0, command=open_doctor_page)
DOCTOR_DETAILS.pack(pady=10)  # Add padding if needed

# Create insurance button within the option frame
INSURANCE = tk.Button(option_frame, text='ADITHYA INSURANCE', font=("bold", 15), fg="black", bd=0, command=insurance_page)
INSURANCE.pack(pady=10)  # Add padding if needed

# Create exit button within the option frame
Exit = tk.Button(option_frame, text='EXIT', font=("bold", 15), fg="black", bd=0,command=exit_program)
Exit.pack(pady=10)  # Add padding if needed

# Pack option frame
option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=250, height=1000)

# Start the tkinter event loop
root.mainloop()