"""
Architect table management for the database system.

This module handles all CRUD operations for the Architect table.
"""


import sqlite3

class Architect():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_table_architect(self):
        """
        Create the Architect table if it doesn't exist.
        
        The table includes fields for architect identification, contact info,
        and hiring date tracking.
        
        Returns:
            None
        """
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Architect(
                    Architect_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Phone_Number TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Hiring_Date TEXT NOT NULL
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an architect table, resulted as {e}")
            raise
            
    def insert_architect_value(self, name: str, phone: str, email: str, hire_date: str):
        """
        Insert a new architect record into the database.
        
        Args:
            name: Full name of the architect
            phone: Contact phone number
            email: Contact email address
            hire_date: Date hired in YYYY-MM-DD format
            
        Returns:
            int: The auto-generated Architect_ID of the new record, or None if failed
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO Architect(Name, Phone_Number, Email, Hiring_Date) VALUES (?, ?, ?, ?)
                """,
                (name, phone, email, hire_date)
            )
            self.db.commit()
            
            return self.cursor.lastrowid
            
        except Exception as e:
            print(f"Failed to insert values inside of the architect table, problem appeared as {e}")
            raise
            
    def update_architect_value(self, architect_id: int, name: str=None, phone: str=None, email: str=None, hire_date: str=None):
        """
        Update an architect's information. Only provided fields are updated.
        
        Args:
            architect_id: ID of the architect to update
            name: New name (optional)
            phone: New phone number (optional)
            email: New email address (optional)
            hire_date: New hiring date (optional)
            
        Returns:
            None
        """
        try:
            updates = []
            params = []
            
            if name is not None:
                updates.append("Name = ?")
                params.append(name)
            if phone is not None:
                updates.append("Phone_Number = ?")
                params.append(phone)
            if email is not None:
                updates.append("Email = ?")
                params.append(email)
            if hire_date is not None:
                updates.append("Hiring_Date = ?")
                params.append(hire_date)
            
            if not updates:
                print("There was nothing to update, no given parameters. Returning...")
                return
            
            params.append(architect_id)
            
            query = f"UPDATE Architect SET {', '.join(updates)} WHERE Architect_ID = ?"
            self.cursor.execute(query, params)
            self.db.commit()
            print(f"Successfully updated architect ID: {architect_id}")
            
        except Exception as e:
            print(f"There was a problem in updating the architect table, problem resulted as {e}")
            raise
    
    def delete_id(self, architect_id: int):
        '''
        This function aims to remove an architect row based on the id
        '''
        try:
            self.cursor.execute(
                "DELETE FROM Architect WHERE Architect_ID = ?", (architect_id,) 
            )
        except Exception as e:
            print(f"Could not delete architect row, occured as {e}")
            raise