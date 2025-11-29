"""
Main SQL database management module.

This module initializes the database connection and provides
methods to query various tables.
"""

import sqlite3
from engineer import Engineer

class SQL():        
    def __init__(self):
        """
        Initialize the SQL database connection and create table instances.
        
        Uses an in-memory SQLite database for temporary storage.
        """
        self.db = sqlite3.connect(":memory:")
        self.cursor = self.db.cursor()
        self.engineer_table = Engineer(self.db)
    
    def show_engineer_table(self):
        """
        Retrieve all records from the Engineer table.
        
        Returns:
            None (prints results or error message)
            
        Note:
            Consider returning the results instead of just executing the query.
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Engineer
                """
            )
        except Exception as e:
            print(f"Failed in getting the values from Engineer table, occured as {e}")
        
    def show_company_table(self):
        """
        Retrieve all records from the Company table.
        
        Returns:
            None (prints results or error message)
            
        Note:
            Consider returning the results instead of just executing the query.
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Company
                """
            )
        except Exception as e:
            print(f"Failed in getting the values from Company table, occured as {e}")
            
    def show_employer_table(self):
        """
        Retrieve all records from the Employer table.
        
        Returns:
            None (prints results or error message)
            
        Note:
            This method was named show_company_table in the original code (duplicate).
            Consider returning the results instead of just executing the query.
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Employer
                """
            )
        except Exception as e:
            print(f"Failed in getting the values from Employer table, occured as {e}")