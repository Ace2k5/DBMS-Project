import sqlite3

class architect():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_table_architect(self):
        '''
        This functions aims to create the architect table. This table will function as a foreign key for the Projects table
        To clarify hiring date, it is how long the architect has been in OUR company.
        '''
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Architect(
                    Architect_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Phone_Number TEXT,
                    Email TEXT,
                    Hiring_Date TEXT
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an architect table, resulted as {e}")
            
    def insert_values_into_architect(self, name: str, phone: str, email: str, hire_date: str):
        '''
        This function will aim to insert values inside of the architect table while grabbing the last row inserted inside of the
        table.
        
            Args:
                name = str, name of the company
                phone = str, the phone number of the architect
                email = str, the email of the architect
                hire_date = str, when the architect was hired into the company
        '''
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
            
    def update_architect_values(self, architect_id: int, name: str=None, phone: str=None, email: str=None, hire_date: str=None):
        '''
        This function will update values based on how many parameters are given.
            Args:
                architect_id = int, the id of the architect
                name = str, the name of the architect
                phone = str, phone number of the architect
                email = str, email of the architect
                hire_date = str, when the architect was hired to the company
        '''
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
            
            query = f"UPDATE architect SET {', '.join(updates)} WHERE architect_ID = ?"
            self.cursor.execute(query, params)
            self.db.commit()
            print(f"Successfully updated architect ID: {architect_id}")
            
        except Exception as e:
            print(f"There was a problem in updating the architect table, problem resulted as {e}")
    
    def delete_id(self, architect_id: int):
        '''
        This function aims to remove an architect row based on the id
        '''
        self.cursor.execute(
            "DELETE FROM Company WHERE architect_ID = ?", (architect_id,) 
        )