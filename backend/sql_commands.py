"""
SQL commands.

This module handles all of the SQL table retrievals
"""

import sqlite3
class SQLDatabaseCommands():
    def __init__(self, db: sqlite3.Connection):
          self.db = db
          self.cursor = self.db.cursor()

    def show_table(self, table_name: str):
        """
        Retrieve all records from tables
        
        Returns:
            Returns table info
            
        """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed in getting the valeus from the {table_name} table, {e}")
