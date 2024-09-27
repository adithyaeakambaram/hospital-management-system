import smtplib
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
import re

db = Database("adithyahospital.db")

# def generatemsg():
#     randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))
#     return randomCode

def sendingMail(receiver, server, details):
    # Construct the message with all the details
    msg = f"Hello!\nAdithya Hospital, your appointment was booked today. Details:\n\n" \
          f"Patient Name: {details['patient_name']}\n" \
          f"Age: {details['age']}\n" \
          f"DOB: {details['dob']}\n" \
          f"Email: {details['email']}\n" \
          f"Gender: {details['gender']}\n" \
          f"Contact: {details['contact']}\n" \
          f"Doctor Name: {details['doctor_name']}\n" \
          f"Specialty: {details['specialty']}\n" \
          f"Timings: {details['timings']}\n" \
          f"Address: {details['address']}\n" \
          f"For more information, contact 9222110"

    # Send the email
    server.sendmail(sender, receiver, msg)


# def checkOTP():
#     if code == codeEntry.get():
#         accept = Label(root, text='Successful Verification!', fg='green', font=('Arial', 20))
#         accept.place(x=230, y=350)
#     else:
#         refuse = Label(root, text='Unsuccessful Verification!', fg='red', font=('Arial', 20))
#         refuse.place(x=230, y=350)


def connectingSender():
    if txt_PATIENT_NAME.get() == "" or txt_age.get() == "" or txt_DOB.get() == "" or txt_email.get() == "" or combogender.get() == "" \
            or txt_contact.get() == "" or txt_doctor_name.get() == "" or txt_specialty.get() == "" or txt_timings.get() == "" or txt_address.get(
        1.0, END) == "":
        messagebox.showerror("Error", "Please fill all the details.")
        return
    elif not txt_PATIENT_NAME.get().isalpha() or not txt_doctor_name.get().isalpha() or not txt_specialty.get().isalpha():
        messagebox.showerror("Invalid Input",
                             "Name, Doctor's Name, and Specialty should contain only alphabetic characters.")
        return
    receiver = txt_email.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    details = {
        "patient_name": txt_PATIENT_NAME.get(),
        "age": txt_age.get(),
        "dob": txt_DOB.get(),
        "email": txt_email.get(),
        "gender": combogender.get(),
        "contact": txt_contact.get(),
        "doctor_name": txt_doctor_name.get(),
        "specialty": txt_specialty.get(),
        "timings": txt_timings.get(),
        "address": txt_address.get(1.0, END)
    }

    # Send the email
    sendingMail(receiver, server, details)
    server.quit()


root = Tk()
root.title("adithya hospital")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

sender = 'eadithya2001@gmail.com'
password = 'cicz takl vquz wbbp'
# code = generatemsg()

# Define global variables
row = None

PATIENT_NAME = StringVar()
AGE = IntVar()
DOB = IntVar()
EMAIL = StringVar()
GENDER = StringVar()
CONTACT = IntVar()
DOCTOR_NAME = StringVar()
SPECIALTY = StringVar()
TIMINGS = StringVar()


# Entries Frame
entry_frame = Frame(root, bg="black")
entry_frame.pack(side=TOP, fill=X)
tittle = Label(entry_frame, text="ADITHYA HOSPITAL", font=("Calibri", 18, "bold"), bg="black", fg="white")
tittle.grid(row=0, columnspan=2, padx=10, pady=20)

lbl_PATIENT_NAME = Label(entry_frame, text="PATIENT_NAME", font=("Calibri", 16), bg="black", fg="white")
lbl_PATIENT_NAME.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txt_PATIENT_NAME = Entry(entry_frame, textvariable=PATIENT_NAME, font=("Calibri", 16), width=30)
txt_PATIENT_NAME.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lbl_age = Label(entry_frame, text="AGE", font=("Calibri", 16), bg="black", fg="white")
lbl_age.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txt_age = Entry(entry_frame, textvariable=AGE, validate="key", font=("Calibri", 16), width=30)
txt_age.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbl_DOB = Label(entry_frame, text="DOB (YYYY-MM-DD)", font=("Calibri", 16), bg="black", fg="white")
lbl_DOB.grid(row=1, column=4, padx=10, pady=10, sticky="w")
txt_DOB = Entry(entry_frame, textvariable=DOB, font=("Calibri", 16), width=30)
txt_DOB.grid(row=1, column=5, padx=10, pady=10, sticky="w")

lbl_email = Label(entry_frame, text="EMAIL", justify=LEFT, font=("Calibri", 16), bg="black", fg="white")
lbl_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txt_email = Entry(entry_frame, textvariable=EMAIL, font=("Calibri", 16), width=30)
txt_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lbl_gender = Label(entry_frame, text="GENDER", font=("Calibri", 16), bg="black", fg="white")
lbl_gender.grid(row=2, column=2, padx=10, pady=10, sticky="w")
combogender = ttk.Combobox(entry_frame, textvariable=GENDER, font=("Calibri", 16, "bold"), width=12, state="readonly")
combogender['values'] = ("Male", "Female")
combogender.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lbl_contact = Label(entry_frame, text="CONTACT", font=("Calibri", 16), bg="black", fg="white")
lbl_contact.grid(row=2, column=4, padx=10, pady=10, sticky="w")
txt_contact = Entry(entry_frame, textvariable=CONTACT, font=("Calibri", 16), width=30)
txt_contact.grid(row=2, column=5, padx=10, pady=10, sticky="w")

lbl_doctor_name = Label(entry_frame, text="DOCTOR_NAMR", font=("Calibri", 16), bg="black", fg="white")
lbl_doctor_name.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txt_doctor_name = Entry(entry_frame, textvariable=DOCTOR_NAME, font=("Calibri", 16), width=30)
txt_doctor_name.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lbl_specialty = Label(entry_frame, text="SPECIALIST", font=("Calibri", 16), bg="black", fg="white")
lbl_specialty.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txt_specialty = Entry(entry_frame, textvariable=SPECIALTY, font=("Calibri", 16), width=30)
txt_specialty.grid(row=3, column=3, padx=10, pady=10, sticky="w")

lbl_timings = Label(entry_frame, text="TIMINGS", font=("Calibri", 16), bg="black", fg="white")
lbl_timings.grid(row=3, column=4, padx=10, pady=10, sticky="w")
txt_timings = Entry(entry_frame, textvariable=TIMINGS, font=("Calibri", 16), width=30)
txt_timings.grid(row=3, column=5, padx=10, pady=10, sticky="w")

lbl_address = Label(entry_frame, text="ADDRESS", font=("Calibri", 16), bg="black", fg="white")
lbl_address.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txt_address = Text(entry_frame, width=85, height=5, font=("Calibri", 16))
txt_address.grid(row=5, column=0, columnspan=6, padx=10, pady=10, sticky="w")


# def send_email_with_details(row):
#     receiver = row[4]  # Assuming the email is stored in the 4th column
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(sender, password)
#     msg = f"Details:\nName: {row[1]}\nAge: {row[2]}\nDOB: {row[3]}\nEmail: {row[4]}\nGender: {row[5]}\nContact: {row[6]}\nDoctor Name: {row[7]}\nSpecialty: {row[8]}\nTimings: {row[9]}\nAddress: {row[10]}"
#     server.sendmail(sender, receiver, msg)
#     server.quit()


def getData(event):
    global row  # Define row as global
    selected_row = tv.focus()
    if selected_row:
        data = tv.item(selected_row)
        row = data['values']  # Update row variable
        PATIENT_NAME.set(row[1])
        AGE.set(row[2])
        DOB.set(row[3])
        EMAIL.set(row[4])
        GENDER.set(row[5])
        CONTACT.set(row[6])
        DOCTOR_NAME.set(row[7])
        SPECIALTY.set(row[8])
        TIMINGS.set(row[9])
        txt_address.delete(1.0, END)
        txt_address.insert(END, row[10])


    else:
        clearAll()


def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)
    clearAll()

def add_hospital_detail():
    global row
    if txt_PATIENT_NAME.get() == "" or txt_age.get() == "" or txt_DOB.get() == "" or txt_email.get() == "" or combogender.get() == "" \
            or txt_contact.get() == "" or txt_doctor_name.get() == "" or txt_specialty.get() == "" or txt_timings.get() == "" or txt_address.get(
        1.0, END) == "":
        messagebox.showerror("Error", "Please fill all the details.")
        return
    elif not txt_PATIENT_NAME.get().isalpha() or not txt_doctor_name.get().isalpha() or not txt_specialty.get().isalpha():
        messagebox.showerror("Invalid Input",
                             "Name, Doctor's Name, and Specialty should contain only alphabetic characters.")
        return
    try:
        int(txt_age.get())
        int(txt_contact.get())
        int(txt_timings.get())
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

    db.insert(txt_PATIENT_NAME.get(), txt_age.get(), txt_DOB.get(), txt_email.get(), combogender.get(),
              txt_contact.get(),
              txt_doctor_name.get(), txt_specialty.get(), txt_timings.get(), txt_address.get(1.0, END))
    messagebox.showinfo("Success", "Record inserted.")
    clearAll()
    dispalyAll()


    # book_appointment_button.config(state="normal")


def update_hospital_detail():
    global row
    if txt_PATIENT_NAME.get() == "" or txt_age.get() == "" or txt_DOB.get() == "" or txt_email.get() == "" or combogender.get() == "" \
            or txt_contact.get() == "" or txt_doctor_name.get() == "" or txt_specialty.get() == "" or txt_timings.get() == "" or txt_address.get(
        1.0, END) == "":
        messagebox.showerror("Error", "Please fill all the details.")
        return
    elif not txt_PATIENT_NAME.get().isalpha() or not txt_doctor_name.get().isalpha() or not txt_specialty.get().isalpha():
        messagebox.showerror("Invalid Input",
                             "Name, Doctor's Name, and Specialty should contain only alphabetic characters.")
        return
    try:
        int(txt_age.get())
        int(txt_contact.get())
        int(txt_timings.get())
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

    db.insert(txt_PATIENT_NAME.get(), txt_age.get(), txt_DOB.get(), txt_email.get(), combogender.get(),
              txt_contact.get(),
              txt_doctor_name.get(), txt_specialty.get(), txt_timings.get(), txt_address.get(1.0, END))
    messagebox.showinfo("Success", "upadted book.")
    clearAll()
    dispalyAll()
    # book_appointment_button.config(state="normal")


def delete_hospital_detail():
    global row  # Define row as global
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    global row  # Define row as global
    PATIENT_NAME.set("")
    AGE.set("")
    DOB.set("")
    EMAIL.set("")
    GENDER.set("")
    CONTACT.set("")
    DOCTOR_NAME.set("")
    SPECIALTY.set("")
    TIMINGS.set("")
    txt_address.delete(1.0, END)
    txt_address.insert(END, "")
    # Check if row is defined before accessing its elements
    # if row:
    #     txt_address.insert(END, row[10])
    # book_appointment_button.config(state="normal")


sender = 'eadithya2001@gmail.com'
password = 'cicz takl vquz wbbp'
# code = generateOTP()

# def book_appointment():
#     global row  # Define row as global
#     if not row:
#         messagebox.showerror("Error", "Please select an employee first.")
#         return
#     else:
#         # Get appointment details from the GUI input fields
#         appointment_date = ""
#         appointment_time = ""
#         patient_name = ""  # Extract patient name from the GUI
#         doctor_name = row[7]  # Assuming doctor's name is stored in row[7] from employee details
#         # Additional appointment details can be extracted similarly
#
#         # Validate appointment details (e.g., check if the appointment date and time are valid)
#
#         # Insert the appointment details into the database
#         # Example code assuming you have a method to insert into the appointment table
#         # db.insert_appointment(appointment_date, appointment_time, patient_name, doctor_name, ...)
#
#         # Provide feedback to the user
#         messagebox.showinfo("Success", "Appointment booked successfully!")
#
#         # Optionally, you can clear the input fields after booking
#         clearAll()
#         # Optionally, you can refresh the displayed appointments in the GUI
#         dispalyAll()

bttn_frame = Frame(entry_frame, bg="white")
bttn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
add_bttn = Button(bttn_frame, command=add_hospital_detail, text="BOOKING", width=10, font=("Calibri", 10, "bold"),
                  bg="black", fg="white", bd=0)
add_bttn.grid(row=0, column=0, padx=10, sticky="w")

edit_bttn = Button(bttn_frame, command=update_hospital_detail, text="UPDATEBOOKING", width=14,
                   font=("Calibri", 10, "bold"), bg="black", fg="white", bd=0)
edit_bttn.grid(row=0, column=1, padx=10, sticky="w")

delete_bttn = Button(bttn_frame, command=delete_hospital_detail, text="CANCELBOOKING", width=14,
                     font=("Calibri", 10, "bold"), bg="black", fg="white", bd=0)
delete_bttn.grid(row=0, column=2, padx=10, sticky="w")

clear_bttn = Button(bttn_frame, command=clearAll, text="CLEARBOOKING", width=14, font=("Calibri", 10, "bold"),
                    bg="black", fg="white", bd=0)
clear_bttn.grid(row=0, column=3, padx=10, sticky="w")

sendOTP = Button(bttn_frame,command=connectingSender, text="SEND EMAIL", width=10,  font=("Calibri", 10,"bold" ), bg="black", fg="white", bd=0)

sendOTP.grid(row=0, column=4, padx=10, sticky="w")


# book_appointment_button = Button(bttn_frame, text="Book Appointment", command=book_appointment, width=15, font=("Calibri", 10, "bold"), bg="black", fg="white", bd=0)
# book_appointment_button.grid(row=0, column=4, padx=10, sticky="w")
# # Initially disable the button
# book_appointment_button.config(state="disabled")

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
# style = ttk.Style()
# style.configure("mystyle.Treeview", font=('Calibri', 18),
#                 rowheight=50)  # Modify the font of the body
# style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18))
# tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="id")
tv.column("1", width=5)
tv.heading("2", text="PATIENT_NAME")
tv.heading("3", text="AGE")
tv.column("1", width=5)
tv.heading("4", text="DOB")
tv.heading("5", text="EMAIL")
tv.heading("6", text="GENDER")
tv.column("1", width=10)
tv.heading("7", text="CONTACT")
tv.heading("8", text="DOCTOR_NAME")
tv.heading("9", text="SPECIALIST")
tv.heading("10", text="TIMINGS")

tv.heading("11", text="ADDRESS")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)
clearAll()
dispalyAll()
root.mainloop()