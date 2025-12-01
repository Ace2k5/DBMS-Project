"""
SQL commands.

This module handles all of the SQL table retrievals
"""

import sqlite3
class SQLDatabaseCommands():
    def __init__(self, db: sqlite3.Connection):
          self.db = db
          self.cursor = self.db.cursor()

    # ENGINEER
    def show_engineer_table(self):
            """
            Retrieve all records from the Engineer table.
            
            Returns:
                Engineer table
            """
            try:
                self.cursor.execute(
                    """
                    SELECT * FROM Engineer
                    """
                )
                return self.cursor.fetchall()
            except Exception as e:
                print(f"Failed in getting the values from Engineer table, occured as {e}")
    #####

    # COMPANY
    def show_company_table(self):
        """
        Retrieve all records from the Company table.
        
        Returns:
            Returns Company Table
            
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Company
                """
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed in getting the values from Company table, occured as {e}")
    ####

    # EMPLOYER
    def show_employer_table(self):
        """
        Retrieve all records from the Employer table.
        
        Returns:
            Returns Employer Table
            
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Employer
                """
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed in getting the values from Employer table, occured as {e}")
    ####
    
    # ARCHITECT
    def show_architect_table(self):
        """
        Retrieve all records from the Architect table.
        
        Returns:
            Returns Architect Table
            
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Architect
                """
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed in getting the values from Architect table, occured as {e}")
    ####
    
    # PROJECT
    def show_project_table(self):
        """
        Retrieve all records from the Project table.
        
        Returns:
            Returns Project Table
            
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM Project
                """
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed in getting the values from Project table, occured as {e}")
    ####