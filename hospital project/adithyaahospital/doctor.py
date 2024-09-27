# import tkinter as tk
# from tkinter import ttk
# import
#
# # Function to search for a doctor by name
# def search():
#     query = search_entry.get()
#     for row in tree.get_children():
#         tree.delete(row)
#     for doctor in get_doctors(query):
#         tree.insert("", "end", values=doctor)
#
# # Creating the tkinter window
# root = tk.Tk()
# root.title("Doctor Details")
#
# # Creating treeview for doctor details
# tree = ttk.Treeview(root, columns=("Name", "Specialist", "Timing"))
# tree.heading("#0", text="Doctor Details", anchor=tk.CENTER)
# tree.heading("Name", text="Name", anchor=tk.CENTER)
# tree.heading("Specialist", text="Specialist", anchor=tk.CENTER)
# tree.heading("Timing", text="Timing", anchor=tk.CENTER)
#
# # Inserting initial doctor details
# for doctor in get_doctors():
#     tree.insert("", "end", values=doctor)
#
# # Creating search box
# search_label = tk.Label(root, text="Search Doctor:")
# search_entry = tk.Entry(root)
# search_button = tk.Button(root, text="Search", command=search)
#
# # Placing widgets on the window
# tree.pack(pady=10)
# search_label.pack()
# search_entry.pack()
# search_button.pack()
#
# root.mainloop()
import tkinter as tk
from tkinter import ttk, PhotoImage
import subprocess
from doctordb import get_doctor_details, insert_doctor_details

# Create the tkinter window
root = tk.Tk()
root.title("ADITHYA HOSPITAL DOCTOR DETAILS")
bg_image = PhotoImage(file=r"C:\Users\vasanth kumar\Downloads\adhi.png")  # replace 'background.png' with your image file
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the doctor details
details_frame = tk.Frame(root)
details_frame.pack()

# Create labels and entry widgets for doctor details
doctor_name_label = tk.Label(details_frame, text="Doctor Name:")
doctor_name_entry = tk.Entry(details_frame)
specialist_label = tk.Label(details_frame, text="Specialist:")
specialist_entry = tk.Entry(details_frame)
timing_label = tk.Label(details_frame, text="Timing:")
timing_entry = tk.Entry(details_frame)

# Position the labels and entry widgets in the grid
doctor_name_label.grid(row=0, column=0)
doctor_name_entry.grid(row=0, column=1)
specialist_label.grid(row=1, column=0)
specialist_entry.grid(row=1, column=1)
timing_label.grid(row=2, column=0)
timing_entry.grid(row=2, column=1)

# Function to handle Add button click
def add_button_click():
    name = doctor_name_entry.get()
    specialist = specialist_entry.get()
    timing = timing_entry.get()
    insert_doctor_details(name, specialist, timing)
    populate_treeview()

# Add button
add_button = tk.Button(details_frame, text="Add", command=add_button_click)
add_button.grid(row=3, column=0, columnspan=2)

# Create a treeview widget to display doctor details
columns = ("DOCTOR_NAME", "SPECIALIST", "TIMINGS")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack()

# Function to populate the treeview with doctor details
def populate_treeview(name=None):
    # Clear existing data
    for row in tree.get_children():
        tree.delete(row)

    # Retrieve doctor details from the database
    doctor_details = get_doctor_details(name)

    # Insert doctor details into the treeview
    for doctor in doctor_details:
        tree.insert("", "end", values=doctor)

# Call the function to populate the treeview initially
populate_treeview()

# Entry widget for user input
entry = tk.Entry(root)
entry.pack()

# Function to handle search
def search():
    doctor_name = entry.get()
    populate_treeview(doctor_name)

# Search button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# Function to handle OK button click
def ok_button_click():
    # Call main.py using subprocess
    subprocess.run(["python", "main.py"])

# OK button
ok_button = tk.Button(root, text="OK", command=ok_button_click)
ok_button.pack()

root.mainloop()