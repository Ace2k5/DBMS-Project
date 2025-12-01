
"""
Engineer table management for the database system.

This module handles all CRUD operations for the Engineer table.
"""
import sqlite3

class Engineer():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
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
            
    def insert_engineer_value(self, name: str, field: str, phone: str, email: str, hire_date: str):
        """
        Insert a new engineer record into the database.
        
        Args:
            name: Full name of the engineer
            field: Engineering specialization (e.g., "Civil", "Mechanical")
            phone: Contact phone number
            email: Contact email address
            hire_date: Date hired in YYYY-MM-DD format
            
        Returns:
            int: The auto-generated Engineer_ID of the new record, or None if failed
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO Engineer(Name, Engineering_Field, Phone_Number, Email, Hiring_Date) VALUES (?, ?, ?, ?, ?)
                """,
                (name, field, phone, email, hire_date)
            )
            self.db.commit()
            
            return self.cursor.lastrowid
            
        except Exception as e:
            print(f"Failed to insert values inside of the Engineering table, problem appeared as {e}")
            raise
            
    def update_engineer_value(self, engineer_id: int, name: str=None, field: str=None, phone: str=None, email: str=None, hire_date: str=None):
        """
        Update an engineer's information. Only provided fields are updated.
        
        Args:
            engineer_id: ID of the engineer to update
            name: New name (optional)
            field: New engineering field (optional)
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
            if field is not None:
                updates.append("Engineering_Field = ?")
                params.append(field)
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
            
            params.append(engineer_id)
            
            query = f"UPDATE Engineer SET {', '.join(updates)} WHERE Engineer_ID = ?"
            self.cursor.execute(query, params)
            self.db.commit()
            print(f"Successfully updated Engineer ID: {engineer_id}")
            
        except Exception as e:
            print(f"There was a problem in updating the Engineering table, problem resulted as {e}")
            raise
    
    def delete_id(self, engineer_id: int):
        """
        Remove an engineer record from the database.
        
        Args:
            engineer_id: ID of the engineer to delete
            
        Returns:
            None
        """
        try:
            self.cursor.execute(
                "DELETE FROM Engineer WHERE Engineer_ID = ?", (engineer_id,) 
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not delete engineer row, occured as {e}")
            raise
        