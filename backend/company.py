'''

The purpose of this file is to input the company that requested the project.

'''

import sqlite3

class Company():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_table_company(self):
        '''
        This functions aims to create the company table. This table will function as a foreign key for the Projects table
        
        '''
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Company(
                    Company_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Company_Name TEXT,
                    Phone_Number TEXT,
                    Email TEXT,
                    Address TEXT,
                    Date_of_Request TEXT
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an Engineering table, resulted as {e}")
            
    def insert_company_value(self, name: str, phone_num: str, email: str, address: str, date: str):
        '''
        This function will aim to insert values inside of the Company table while grabbing the last row inserted inside of the
        table.
            Args:
                company_id = int, the id of the company
                name = str, name of the company
                phone_num = str, phone number of the company
                email = str, email of the company
                address = str, where the company is located
                date = str, when the company requested for the project
        '''
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
            
    def update_company_value(self, company_id: int, name: str=None, phone_num: str=None, email: str=None, address: str=None, date: str=None):
        '''
        This function will update values based on how many parameters are given.

            Args:
                company_id = int, the id of the company
                name = str, name of the company
                phone_num = str, phone number of the company
                email = str, email of the company
                address = str, where the company is located
                date = str, when the company requested for the project
        '''
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
            
    def delete_id(self, company_id: int):
        '''
        This function aims to remove a company row based on the id
        '''
        self.cursor.execute(
            "DELETE FROM Company WHERE Company_ID = ?", (company_id,) 
        )