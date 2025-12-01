
"""
Employer table management for the database system.

This module handles all CRUD operations for the Employer table.
"""

import sqlite3

class Employer():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
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
            
    
    def insert_employer_value(self, name: str, email: str, phone: str, hiring_date: str):
        """
        Insert a new employer record into the database.
        
        Args:
            name: Full name of the employer
            email: Contact email address
            phone: Contact phone number
            hiring_date: Date hired in YYYY-MM-DD format
            
        Returns:
            int: The auto-generated Employer_ID of the new record, or None if failed
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO Employer(Employer_Name, Email, Phone, Hiring_Date) VALUES (?, ?, ?, ?) 
                """,
                (name, email, phone, hiring_date)
            )
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"An error occured when inserting values into Employer table, problem appeared as {e}")
            raise
            
    def update_employer_value(self, employer_id: int, name: str=None, email: str=None, phone: str=None, hiring_date: str=None):
        """
        Update an employer's information. Only provided fields are updated.
        
        Args:
            employer_id: ID of the employer to update
            name: New name (optional)
            email: New email address (optional)
            phone: New phone number (optional)
            hiring_date: New hiring date (optional)
            
        Returns:
            None
        """
        try:
            updates = []
            params = []
            
            if name is not None:
                updates.append("Employer_Name = ?")
                params.append(name)
            if email is not None:
                updates.append("Email = ?")
                params.append(email)
            if phone is not None:
                updates.append("Phone = ?")
                params.append(phone)
            if hiring_date is not None:
                updates.append("Hiring_Date = ?")
                params.append(hiring_date)
            
            
            if not updates:
                print("There was nothing to update, no given parameters. Returning...")
                return
            
            params.append(employer_id)
            
            query = f"UPDATE Employer SET {', '.join(updates)} WHERE Employer_ID = ?"
            self.cursor.execute(query, params)
            self.db.commit()
            print(f"Successfully updated Engineer ID: {employer_id}")
        except Exception as e:
            print(f"Could not update company table, problem appeared as {e}")
            raise
        
        
    def delete_id(self, employer_id: int):
        """
        Remove an employer record from the database.
        
        Args:
            employer_id: ID of the employer to delete
            
        Returns:
            None
        """
        try:
            self.cursor.execute(
                "DELETE FROM Employer WHERE Employer_ID = ?", (employer_id,) 
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not delete employer row, occured as {e}")
            raise