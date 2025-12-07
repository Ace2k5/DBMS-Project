"""
Project table management for the database system.

This module handles all CRUD operations for the Project table,
which links together Engineer, Architect, Company, and Employer tables.
"""

import sqlite3
from backend.db_table import BaseTable
class Project(BaseTable):
    def __init__(self, db: sqlite3.Connection, cursor: sqlite3.Cursor):
        super().__init__(db, cursor, table_name="Project", pk="Project_ID")
        
    def create_table(self):
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
                    Budget TEXT NOT NULL
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not create the projects table, occured as {e}")
            raise