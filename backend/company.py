"""
Company table management for the database system.

This module handles all CRUD operations for the Company table.
"""

import sqlite3
from backend.db_table import BaseTable

class Company(BaseTable):
    def __init__(self, db: sqlite3.Connection, cursor: sqlite3.Cursor):
        super().__init__(db, cursor, table_name="Company", pk="Company_ID")
        
    def create_table(self):
        """
        Create the Company table if it doesn't exist.
        
        The table includes fields for company identification, contact info,
        address, and request date tracking.
        
        Returns:
            None
        """

        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Company(
                    Company_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Company_Name TEXT NOT NULL,
                    Phone_Number TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Address TEXT NOT NULL,
                    Date_of_Request TEXT NOT NULL
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an Engineering table, resulted as {e}")
            raise