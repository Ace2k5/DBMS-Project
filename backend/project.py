"""
Project table management for the database system.

This module handles all CRUD operations for the Project table,
which links together Engineer, Architect, Company, and Employer tables.
"""

import sqlite3
from .db_table import BaseTable
class Project(BaseTable):
    def __init__(self, db: sqlite3.Connection):
        super().__init__(db, table_name="Project", pk="Project_ID")
        
    def create_project_table(self):
        """
        Create the Project table if it doesn't exist.
        
        The table uses foreign keys to reference Company, Employer, Engineer,
        and Architect tables, establishing relationships between entities.
        
        Returns:
            None
        """
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Project(
                    Project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Project_Name TEXT NOT NULL,
                    Budget TEXT NOT NULL,
                    Company_ID INTEGER NOT NULL,
                    Employer_ID INTEGER NOT NULL,
                    Engineer_ID INTEGER NOT NULL,
                    Architect_ID INTEGER NOT NULL,
                    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID),
                    FOREIGN KEY (Employer_ID) REFERENCES Employer(Employer_ID),
                    FOREIGN KEY (Engineer_ID) REFERENCES Engineer(Engineer_ID),
                    FOREIGN KEY (Architect_ID) REFERENCES Architect(Architect_ID),
                    Is_Done TEXT NOT NULL
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not create the projects table, occured as {e}")
            raise