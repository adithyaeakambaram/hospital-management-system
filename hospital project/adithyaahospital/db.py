import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS hospitaldetails (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, dob TEXT, email TEXT, gender TEXT, contact INTEGER, doctor_name TEXT, specialty TEXT, timings TEXT, address TEXT)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM hospitaldetails")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, age, dob, email, gender, contact, doctor_name, specialty, timings, address):
        self.cur.execute("INSERT INTO hospitaldetails VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",
                         (name, age, dob, email, gender, contact, doctor_name, specialty, timings, address))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM hospitaldetails WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, age, dob, email, gender, contact, doctor_name, specialty, timings, address):
        self.cur.execute("UPDATE hospitaldetails SET name=?, age=?, dob=?, email=?, gender=?, contact=?, doctor_name=?, specialty=?, timings=?, address=? WHERE id=?",
                         (name, age, dob, email, gender, contact, doctor_name, specialty, timings, address, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()