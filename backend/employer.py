'''

The purpose of this file is to input the employer that handled the company request.

'''

import sqlite3

class Employer():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_employer_table(self):
        '''
        This functions aims to create the employer table. This table will function as a foreign key for the Projects table
        To clarify hiring date, it is how long the employer has been in OUR company.
        '''
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Employer(
                    Employer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Employer_Name TEXT,
                    Email TEXT,
                    Phone TEXT,
                    Hiring_Date TEXT
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failed to create employer table, problem occured as {e}")
            raise
    
    def insert_employer_value(self, name: str, email: str, phone: str, hiring_date: str):
        '''
        This function will aim to insert values inside of the Engineering table while grabbing the last row inserted inside of the
        table.
        
            Args:
                name = str, name of the employer
                email = str, the email of the employer
                phone = str, the phone number of the employer
                hire_date = str, when the employer was hired into the company
        '''
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
        '''
        This function will aim to update values inside of the Employer table.
        
            Args:
                name = str, name of the employer
                email = str, the email of the employer
                phone = str, the phone number of the employer
                hire_date = str, when the employer was hired into the company
        '''
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
        '''
        This function aims to remove an employer row based on the id
            Args:
                employer_id = int, id of the employer that the user wants to remove
        '''
        try:
            self.cursor.execute(
                "DELETE FROM Employer WHERE Employer_ID = ?", (employer_id,) 
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not delete employer row, occured as {e}")
            raise