
"""
Employer table management for the database system.

This module handles all CRUD operations for the Employer table.
"""

import sqlite3
from .db_table import BaseTable

class Employer(BaseTable):
    def __init__(self, db: sqlite3.Connection):
        super().__init__(db, table_name="Employer", pk="Employer_ID")
        
    def create_employer_table(self):
        """
        Create the Employer table if it doesn't exist.
        
        The table includes fields for employer identification, contact info,
        and hiring date tracking.
        
        Returns:
            None
        """
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Employer(
                    Employer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Employer_Name TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Phone TEXT NOT NULL,
                    Hiring_Date TEXT NOT NULL
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failed to create employer table, problem occured as {e}")