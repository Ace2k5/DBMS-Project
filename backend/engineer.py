
"""
Engineer table management for the database system.

This module handles all CRUD operations for the Engineer table.
"""
import sqlite3
from .db_table import BaseTable

class Engineer(BaseTable):
    def __init__(self, db: sqlite3.Connection):
        super().__init__(db, table_name="Engineer", pk="Engineer_ID")
        
    def create_table_engineer(self):
        """
        Create the Engineer table if it doesn't exist.
        
        The table includes fields for engineer identification, contact info,
        and hiring date tracking.
        
        Returns:
            None
        """
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Engineer(
                    Engineer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Engineering_Field TEXT NOT NULL,
                    Phone_Number TEXT NOT NULL,
                    Email TEXT NOT NULL, 
                    Hiring_Date TEXT NOT NULL
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an Engineering table, resulted as {e}")
            raise