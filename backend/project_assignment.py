import sqlite3
from .db_table import BaseTable

class ProjectAssignment(BaseTable):
    def __init__(self, db: sqlite3.Connection, cursor: sqlite3.Cursor):
        super().__init__(db, cursor, table_name="ProjectAssignment", pk="ProjectAssignment_ID")

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS ProjectAssignment(
                    ProjectAssignment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Company_ID INTEGER,
                    Project_ID INTEGER,
                    Person_ID INTEGER,
                    Is_Done TEXT NOT NULL,
                    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID) ON DELETE CASCADE,
                    FOREIGN KEY (Project_ID) REFERENCES Project(Project_ID) ON DELETE CASCADE,
                    FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID) ON DELETE CASCADE
                )
            """)
            self.db.commit()
        except Exception as e:
            print(f"Could not create Project Assignment table: {e}")
            raise
