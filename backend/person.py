import sqlite3
from backend.db_table import BaseTable

class Person(BaseTable):
    def __init__(self, db: sqlite3.Connection, cursor: sqlite3.Cursor):
        super().__init__(db, cursor, table_name="Person", pk="Person_ID")

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Person(
                    Person_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Phone_Number TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Role TEXT NOT NULL,
                    Hiring_Date TEXT NOT NULL
                )
            """)
            self.db.commit()
        except Exception as e:
            print(f"Could not create Person table: {e}")
            raise
