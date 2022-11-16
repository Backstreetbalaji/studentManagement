import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('DATABASE.db')

    def connect_database(self):
        print("OPENED DATABASE SUCCESSFULLY\n")
        return self.conn

    def creating_table(self):
        self.conn = sqlite3.connect('DATABASE.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT_DATABASE
                 (name  TEXT    NOT NULL,
                 age    INT     NOT NULL,
                 number  INT     NOT NULL);''')
        print("Table Created Successfully...\n")

    def insert_into_database(self, n, a, nu):
        self.conn = sqlite3.connect('DATABASE.db')
        self.conn.execute("INSERT INTO STUDENT_DATABASE (name, age , number) \
            VALUES (?,?,?)", (n, a, nu))
        self.conn.commit()
        print("INSERT THE STUDENT DETAILS SUCCESSFULLY")

    def delete_from_database(self, delete_name):
        self.conn = sqlite3.connect('DATABASE.db')
        self.conn.execute("DELETE FROM STUDENT_DATABASE WHERE NAME = ?", (delete_name,))
        print("Student name has been deleted")
        self.conn.commit()

    def show_database(self):
        self.conn = sqlite3.connect('DATABASE.db')
        self.conn.execute("SELECT * FROM STUDENT_DATABASE")
        output = self.conn.execute("SELECT * FROM STUDENT_DATABASE")
        for row in output:
            print(row)
        self.conn.commit()

    def search_from_database(self, search_name):
        self.conn = sqlite3.connect('DATABASE.db')
        self.conn.execute("SELECT * FROM STUDENT_DATABASE WHERE NAME = ?", (search_name,))
        output = self.conn.execute("SELECT * FROM STUDENT_DATABASE WHERE NAME = ?", (search_name,))
        print(output.fetchall())
        result = output.fetchall()
        return result
        self.conn.commit()


