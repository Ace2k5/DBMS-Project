"""
Company table management for the database system.

This module handles all CRUD operations for the Company table.
"""

import sqlite3

class Company():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_table_company(self):
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
            
    def insert_company_value(self, name: str, phone_num: str, email: str, address: str, date: str):
        """
        Insert a new company record into the database.
        
        Args:
            name: Name of the company
            phone_num: Contact phone number
            email: Contact email address
            address: Physical address of the company
            date: Date the company requested the project in YYYY-MM-DD format
            
        Returns:
            int: The auto-generated Company_ID of the new record, or None if failed
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO Company(Company_Name, Phone_Number, Email, Address, Date_of_Request) VALUES (?, ?, ?, ?, ?)
                """,
                (name, phone_num, email, address, date)
            )
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"Failure in inserting values inside of the company table, problem occured as {e}")
            raise
            
    def update_company_value(self, company_id: int, name: str=None, phone_num: str=None, email: str=None, address: str=None, date: str=None):
        """
        Update a company's information. Only provided fields are updated.
        
        Args:
            company_id: ID of the company to update
            name: New company name (optional)
            phone_num: New phone number (optional)
            email: New email address (optional)
            address: New physical address (optional)
            date: New request date (optional)
            
        Returns:
            None
        """
        try:
            updates = []
            params = []
            
            if name is not None:
                updates.append("Company_Name = ?")
                params.append(name)
            if phone_num is not None:
                updates.append("Phone_Number = ?")
                params.append(phone_num)
            if email is not None:
                updates.append("Email = ?")
                params.append(email)
            if address is not None:
                updates.append("Address = ?")
                params.append(address)
            if date is not None:
                updates.append("Date_of_Request = ?")
                params.append(date)
            
            if not updates:
                print("There was nothing to update, no given parameters. Returning...")
                return
            
            params.append(company_id)
            
            query = f"UPDATE Company SET {', '.join(updates)} WHERE Company_ID = ?"
            self.cursor.execute(query, params)
            self.db.commit()
            print(f"Successfully updated Engineer ID: {company_id}")
        except Exception as e:
            print(f"Could not update company table, problem appeared as {e}")
            raise
            
    def delete_id(self, company_id: int):
        '''
        This function aims to remove a company row based on the id
        '''
        try:
            self.cursor.execute(
                "DELETE FROM Company WHERE Company_ID = ?", (company_id,) 
            )
        except Exception as e:
            print(f"Could not delete Company row, occured as {e}")
            raise