from tkinter import *
from tkinter import ttk
from insurancedb import Database
from tkinter import messagebox
import tkinter as tk
import re

db = Database("adithyahospital Insurance.db")
root = Tk()
root.title("Adithya Hospital")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

option_frame = tk.Frame(root, bg="black")
option_frame.pack(side=tk.RIGHT)
option_frame.pack_propagate(False)
option_frame.configure(width=950, height=1000)

NAME = StringVar()
AGE = IntVar()
DOB = StringVar()
EMAIL = StringVar()
GENDER = StringVar()
CONTACT = IntVar()
POLICY_NAME = StringVar()
POLICY_AMOUNT = IntVar()
COVERAGE_AMOUNT = IntVar()

# Entries Frame
entry_frame = Frame(root, bg="black")
entry_frame.pack(side=TOP, fill=X)
title = Label(entry_frame, text="ADITHYA HOSPITAL INSURANCE", font=("Calibri", 18, "bold"), bg="black", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20)

lbl_NAME = Label(entry_frame, text="NAME", font=("Calibri", 16), bg="black", fg="white")
lbl_NAME.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txt_NAME = Entry(entry_frame, textvariable=NAME, font=("Calibri", 16), width=30)
txt_NAME.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lbl_age = Label(entry_frame, text="AGE", font=("Calibri", 16), bg="black", fg="white")
lbl_age.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txt_age = Entry(entry_frame, textvariable=AGE, validate="key", font=("Calibri", 16), width=30)
txt_age.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lbl_DOB = Label(entry_frame, text="DOB (YYYY-MM-DD)", font=("Calibri", 16), bg="black", fg="white")
lbl_DOB.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txt_DOB = Entry(entry_frame, textvariable=DOB, font=("Calibri", 16), width=30)
txt_DOB.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lbl_email = Label(entry_frame, text="EMAIL", justify=LEFT, font=("Calibri", 16), bg="black", fg="white")
lbl_email.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txt_email = Entry(entry_frame, textvariable=EMAIL, font=("Calibri", 16), width=30)
txt_email.grid(row=4, column=1, padx=10, pady=10, sticky="w")

lbl_gender = Label(entry_frame, text="GENDER", font=("Calibri", 16), bg="black", fg="white")
lbl_gender.grid(row=5, column=0, padx=10, pady=10, sticky="w")
combogender = ttk.Combobox(entry_frame, textvariable=GENDER, font=("Calibri", 16, "bold"), width=12, state="readonly")
combogender['values'] = ("Male", "Female")
combogender.grid(row=5, column=1, padx=10, pady=10, sticky="w")

lbl_contact = Label(entry_frame, text="CONTACT", font=("Calibri", 16), bg="black", fg="white")
lbl_contact.grid(row=6, column=0, padx=10, pady=10, sticky="w")
txt_contact = Entry(entry_frame, textvariable=CONTACT, font=("Calibri", 16), width=30)
txt_contact.grid(row=6, column=1, padx=10, pady=10, sticky="w")

lbl_POLICY_name = Label(entry_frame, text="POLICY_NAME", font=("Calibri", 16), bg="black", fg="white")
lbl_POLICY_name.grid(row=7, column=0, padx=10, pady=10, sticky="w")
txt_POLICY_name = Entry(entry_frame, textvariable=POLICY_NAME, font=("Calibri", 16), width=30)
txt_POLICY_name.grid(row=7, column=1, padx=10, pady=10, sticky="w")

lbl_POLICY_AMOUNT = Label(entry_frame, text="POLICY AMOUNT", font=("Calibri", 16), bg="black", fg="white")
lbl_POLICY_AMOUNT.grid(row=8, column=0, padx=10, pady=10, sticky="w")
txt_POLICY_AMOUNT = Entry(entry_frame, textvariable=POLICY_AMOUNT, font=("Calibri", 16), width=30)
txt_POLICY_AMOUNT.grid(row=8, column=1, padx=10, pady=10, sticky="w")

lbl_COVERAGE = Label(entry_frame, text="COVERAGE", font=("Calibri", 16), bg="black", fg="white")
lbl_COVERAGE.grid(row=9, column=0, padx=10, pady=10, sticky="w")
txt_COVERAGE = Entry(entry_frame, textvariable=COVERAGE_AMOUNT, font=("Calibri", 16), width=30)
txt_COVERAGE.grid(row=9, column=1, padx=10, pady=10, sticky="w")

def register():
    if txt_NAME.get() == "" or txt_age.get() == "" or txt_DOB.get() == "" or txt_email.get() == "" or combogender.get() == "" \
            or txt_contact.get() == "" or txt_POLICY_name.get() == "" or txt_POLICY_AMOUNT.get() == "" or txt_COVERAGE.get() == "":
        messagebox.showerror("Error", "Please fill all the details.")
        return
    elif not txt_NAME.get().isalpha() or not txt_POLICY_name.get().isalpha():
        messagebox.showerror("Invalid Input",
                             "Name and Doctor's Name should contain only alphabetic characters.")
        return
    try:
        int(txt_age.get())
        int(txt_contact.get())
        int(txt_COVERAGE.get())
        year, month, day = txt_DOB.get().split("-")
        int(year)
        int(month)
        int(day)

        if not (1 <= int(month) <= 12):
            raise ValueError("Invalid month")
        if not (1 <= int(day) <= 31):
            raise ValueError("Invalid day")
        if not re.match(r"^\d{10}$", txt_contact.get()):
            messagebox.showerror("Error", "Please enter a 10-digit contact number.")
            return

    except ValueError:
        messagebox.showerror("Invalid Input",
                             "Age, contact, and DOB must be integers. DOB format should be YYYY-MM-DD.")
        return

    db.insert(txt_NAME.get(), txt_age.get(), txt_DOB.get(), txt_email.get(), combogender.get(),
              txt_contact.get(), txt_POLICY_name.get(), txt_POLICY_AMOUNT.get(), txt_COVERAGE.get())
    messagebox.showinfo("Success", "Record inserted.")
    clear()

def clear():
    # Clear all the entry fields
    txt_NAME.delete(0, END)
    txt_age.delete(0, END)
    txt_DOB.delete(0, END)
    txt_email.delete(0, END)
    combogender.set('')
    txt_contact.delete(0, END)
    txt_POLICY_name.delete(0, END)
    txt_POLICY_AMOUNT.delete(0, END)
    txt_COVERAGE.delete(0, END)

# Buttons for registering and clearing
bttn_frame = Frame(entry_frame, bg="black")
bttn_frame.grid(row=10, column=1, columnspan=4, padx=10, pady=10, sticky="w")

register_button = Button(bttn_frame, command=register, text="REGISTER", width=15, font=("Calibri", 10, "bold"),
                         bg="white", fg="black", bd=0)
register_button.grid(row=10, column=1, padx=10, sticky="w")

clear_button = Button(bttn_frame, command=clear, text="CLEAR", width=15, font=("Calibri", 10, "bold"),
                      bg="white", fg="black", bd=0)
clear_button.grid(row=10, column=2, padx=10, sticky="w")

# Policy details display frame
def display_policy_details(policy_name):
    # Clear existing labels
    for widget in option_frame.winfo_children():
        widget.destroy()

    # Fetch policy details
    policy_details = db.get_policy_details(policy_name)

    # Display policy name
    policy_label = Label(option_frame, text=policy_name, font=("Calibri", 16, "bold"), bg="GRAY", fg="white")
    policy_label.pack(pady=10)

    # Display age range and coverage amount
    displayed_details = set()
    for age_range, coverage_amount in policy_details:
        detail = f"Age Range: {age_range}, Coverage Amount: {coverage_amount}"
        if detail not in displayed_details:
            detail_label = Label(option_frame, text=detail, font=("Calibri", 12), bg="GRAY", fg="white")
            detail_label.pack(pady=5)
            displayed_details.add(detail)

# Callback function for policy selection
def on_policy_selected(event):
    selected_policy = policy_combobox.get()
    display_policy_details(selected_policy)

# Create combobox for policy selection
policy_options = ["Full Health Insurance", "Accident Policy"]
policy_combobox = ttk.Combobox(entry_frame, values=policy_options)
policy_combobox.bind("<<ComboboxSelected>>", on_policy_selected)
policy_combobox.grid(row=11, column=1, padx=10, pady=10, sticky="w")

root.mainloop()
