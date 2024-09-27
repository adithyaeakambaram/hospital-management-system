# import sqlite3
# class Database:
#     def __init__(self,db):
#         self.con = sqlite3.connect(db)
#         self.cur = self.con.cursor()
#
#         sql = """
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY,
#             username TEXT,
#             password TEXT
#         )
#         """
#         self.cur.execute(sql)
#         self.con.commit()
#
#     def insert_user(self, username, password):
#         self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
#         self.con.commit()
#
#     def fetch_user(self, username, password):
#         self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#         user = self.cur.fetchone()
#         return user

import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert_user(self, username, password):
        self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
        self.con.commit()

    def fetch_user(self, username, password):
        self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cur.fetchone()
        return user