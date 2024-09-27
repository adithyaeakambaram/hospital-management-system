# import tkinter as tk
# from logindb import Database
# from tkinter import messagebox
# from tkinter import PhotoImage
# import subprocess
#
# kk = Database("user.kk")
#
# root = tk.Tk()
# root.title("ADITHYA HOSPITAL")
# root.geometry("400x200")
#
# # Load the background image
# bg_image = PhotoImage(file=r"C:\Users\vasanth kumar\OneDrive\Pictures\1_xMuIOwjliGUPjkzukeWKfw.png")  # replace 'background.png' with your image file
# bg_label = tk.Label(root, image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# username_label = tk.Label(root, text="ADMIN:")
# username_label.pack()
#
# username_entry = tk.Entry(root)
# username_entry.pack()
#
# password_label = tk.Label(root, text="Password:")
# password_label.pack()
#
# password_entry = tk.Entry(root)
# password_entry.pack()
#
# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#
#     if username == "none" and password == "none":
#         messagebox.showinfo("Login Successful", "Welcome,ADITHYA HOSPITAL ADMIN")
#         subprocess.Popen(['python', 'adithyahospitalinfo.py'])
#
#     else:
#         messagebox.showerror("Login Failed", "Invalid username or password")
#
# login_button = tk.Button(root, text="Login", command=login)
# login_button.pack()
#
# root.mainloop()

import tkinter as tk
from logindb import Database
from tkinter import messagebox
from tkinter import PhotoImage
import subprocess

# Initialize the database
kk = Database("user.kk")

# Create the main login window
root = tk.Tk()
root.title("ADITHYA HOSPITAL")
root.geometry("400x200")


# Load the background image
bg_image = PhotoImage(file=r"C:\Users\vasanth kumar\OneDrive\Pictures\1_xMuIOwjliGUPjkzukeWKfw.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to handle registration
def register():
    def register_user():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            kk.insert_user(username, password)
            messagebox.showinfo("Registration Successful", "Account created successfully!")
            register_window.destroy()
            # Open the new page after successful registration
            subprocess.Popen(['python', 'insurance.py'])  # Change 'new_page.py' to the name of your new page file
        else:
            messagebox.showerror("Registration Failed", "Username and password cannot be empty.")

    # Create a registration window
    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("300x150")

    # Username entry field
    username_label = tk.Label(register_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    # Password entry field
    password_label = tk.Label(register_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()

    # Button to submit registration
    register_button = tk.Button(register_window, text="Register", command=register_user)
    register_button.pack()

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "none" and password == "none":
        messagebox.showinfo("Login Successful", "Welcome, ADITHYA HOSPITAL ADMIN")
        subprocess.Popen(['python', 'adithyahospitalinfo.py'])
    else:
        user = kk.fetch_user(username, password)
        if user:
            messagebox.showinfo("Login Successful", "Welcome, " + username)
            subprocess.Popen(['python', 'adithyahospitalinfo.py'])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Username entry field
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password entry field
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Register button
register_button = tk.Button(root, text="CREATE ACCOUNT", command=register)
register_button.pack()

root.mainloop()