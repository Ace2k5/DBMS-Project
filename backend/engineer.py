import sqlite3

class Engineer():
    def __init__(self, db = sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_table_engineer(self):
        '''
        This functions aims to create the engineering table. This table will function as a foreign key for the Projects table
        
        '''
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Engineer(
                    Engineer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Engineering_Field TEXT,
                    Origin_Company TEXT,
                    Hiring_Date TEXT,
                    Is_Complete INTEGER
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Failure in creating an Engineering table, resulted as {e}")
            
    def insert_values_into_engineer(self, name: str, field: str, company: str, hire_date: str, is_done: int):
        '''
        This function will aim to insert values inside of the Engineering table while grabbing the last row inserted inside of the
        table.
        '''
        try:
            self.cursor.execute(
                """
                INSERT INTO Engineer(Name, Engineering_Field, Origin_Company, Hiring_Date, Is_Complete)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, field, company, hire_date, is_done)
            )
            self.db.commit()
            
            return self.cursor.lastrowid
            
        except Exception as e:
            print(f"Failed to insert values inside of the Engineering table, problem appeared as {e}")
            
    def update_engineer_values(self, engineer_id: int, name: str=None, field: str=None, company: str=None, hire_date: str=None, is_done: int=None):
        '''
        This function will update values based on how many parameters are given.
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
            if company is not None:
                updates.append("Origin_Company = ?")
                params.append(company)
            if hire_date is not None:
                updates.append("Hiring_Date = ?")
                params.append(hire_date)    
            if is_done is not None:
                updates.append("Is_Complete = ?")
                params.append(is_done)
            
            if not updates:
                print("There was nothing to update, no given parameters. Returning...")
                return
            
            params.append(engineer_id)
            
            executables = f"UPDATE Engineer SET {', '.join(updates)} WHERE Engineer_ID = ?"
            self.cursor.execute(executables, params)
            self.db.commit()
            print(f"Successfully updated Engineer ID: {engineer_id}")
            
        except Exception as e:
            print(f"There was a problem in updating the Engineering table, problem resulted as {e}")