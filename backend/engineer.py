'''

The purpose of this file is to input the engineer that was assigned to the project.

'''

import sqlite3

class Engineer():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_table_engineer(self):
        '''
        This functions aims to create the engineering table. This table will function as a foreign key for the Projects table
        To clarify hiring date, it is how long the engineer has been in OUR company.
        '''
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Engineer(
                    Engineer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Engineering_Field TEXT,
                    Phone_Number TEXT,
                    Email TEXT,
                    Hiring_Date TEXT
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an Engineering table, resulted as {e}")
            
    def insert_engineer_value(self, name: str, field: str, phone: str, email: str, hire_date: str):
        '''
        This function will aim to insert values inside of the Engineering table while grabbing the last row inserted inside of the
        table.
        
            Args:
                name = str, name of the company
                field = str, field of engineering
                phone = str, the phone number of the engineer
                email = str, the email of the engineer
                hire_date = str, when the engineer was hired into the company
        '''
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
            
    def update_engineer_value(self, engineer_id: int, name: str=None, field: str=None, phone: str=None, email: str=None, hire_date: str=None):
        '''
        This function will update values based on how many parameters are given.
            Args:
                engineer_id = int, the id of the engineer
                name = str, the name of the engineer
                field = str, what field the engineer studied
                phone = str, phone number of the engineer
                email = str, email of the engineer
                hire_date = str, when the engineer was hired to the company
        '''
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
    
    def delete_id(self, engineer_id: int):
        '''
        This function aims to remove an engineer row based on the id
        '''
        self.cursor.execute(
            "DELETE FROM Engineer WHERE Engineer_ID = ?", (engineer_id,) 
        )