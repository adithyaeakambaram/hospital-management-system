import sqlite3

# Create a connection to the database
conn = sqlite3.connect('doctor_details.db')
c = conn.cursor()

# Create a table to store doctor details if not exists
c.execute('''CREATE TABLE IF NOT EXISTS doctors (
                Name TEXT,
                Specialist TEXT,
                Timing TEXT
            )''')
conn.commit()

# Function to insert doctor details into the database
def insert_doctor_details(name, specialist, timing):
    c.execute("INSERT INTO doctors (Name, Specialist, Timing) VALUES (?, ?, ?)", (name, specialist, timing))
    conn.commit()

# Function to retrieve doctor details from the database
def get_doctor_details(name=None):
    if name:
        c.execute("SELECT * FROM doctors WHERE Name=?", (name,))
    else:
        c.execute("SELECT * FROM doctors")
    return c.fetchall()