import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS hospitaldetails (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER,
                            dob TEXT,
                            email TEXT,
                            gender TEXT,
                            contact INTEGER,
                            policy_name TEXT,
                            policy_amount INTEGER,
                            coverage_amount INTEGER
                        )''')
        self.conn.commit()

        # Check if the Insurance table exists, if not, create it and populate with initial data
        self.cur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Insurance' ''')
        if self.cur.fetchone()[0] == 0:
            self.cur.execute('''CREATE TABLE Insurance (
                                    ID INTEGER PRIMARY KEY,
                                    Name TEXT,
                                    AgeRange TEXT,
                                    CoverageAmount INTEGER,
                                    DepositAmount INTEGER
                                )''')

            # Define age brackets and corresponding coverage and deposit amounts for Full Health Insurance
            full_health_age_brackets = [
                (1, 10, 100000, 45000),
                (11, 20, 90000, 45000),
                (21, 30, 80000, 45000),
                (31, 40, 70000, 45000),
                (41, 50, 60000, 45000)
            ]

            # Insert age-based coverage and deposit amounts for Full Health Insurance into the table
            for bracket in full_health_age_brackets:
                self.cur.execute('''INSERT INTO Insurance (Name, AgeRange, CoverageAmount, DepositAmount)
                                    VALUES (?, ?, ?, ?)''',
                                 ('Full Health Insurance', f"{bracket[0]}-{bracket[1]}", bracket[2], bracket[3]))

            # Define age brackets and corresponding coverage and deposit amounts for Accident Policy
            accident_age_brackets = [
                (1, 10, 100000, 45000),
                (11, 20, 90000, 45000),
                (21, 30, 80000, 45000),
                (31, 40, 70000, 45000),
                (41, 50, 60000, 45000)
            ]

            # Insert age-based coverage and deposit amounts for Accident Policy into the table
            for bracket in accident_age_brackets:
                self.cur.execute('''INSERT INTO Insurance (Name, AgeRange, CoverageAmount, DepositAmount)
                                    VALUES (?, ?, ?, ?)''',
                                 ('Accident Policy', f"{bracket[0]}-{bracket[1]}", bracket[2], bracket[3]))

            # Commit changes to the database
            self.conn.commit()

    def insert(self, name, age, dob, email, gender, contact, policy_name, policy_amount, coverage_amount):
        self.cur.execute('''INSERT INTO hospitaldetails (name, age, dob, email, gender, contact, policy_name, policy_amount, coverage_amount)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                         (name, age, dob, email, gender, contact, policy_name, policy_amount, coverage_amount))
        self.conn.commit()

    def get_policy_details(self, policy_name):
        self.cur.execute('''SELECT AgeRange, CoverageAmount FROM Insurance WHERE Name = ?''', (policy_name,))
        return self.cur.fetchall()

