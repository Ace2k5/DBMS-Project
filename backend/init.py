import sqlite3

class SQL():
    def __init__(self):
        self.db = sqlite3.connect(":memory:")
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
                """
                (name, field, company, hire_date, is_done)
            )
            self.db.commit()
            
            return self.cursor.lastrowid
            
        except Exception as e:
            print(f"Failed to insert values inside of the Engineering table, problem appeared as {e}")
            
    def update_engineer_values(self, name: str=None, field: str=None, company: str=None, hire_date: str=None, is_done: int=None):
        '''
        This function will aim to update values based on how many parameters are given.
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
                updates.append("Hiring_Date = ?")
                params.append(hire_date)
            if is_done is not None:
                updates.append("Is_Complete")
                params.append(is_done)
            
            if not updates:
                print("There was nothing to update, no given parameters. Returning...")
                return
            
            executables = f"UPDATE Engineer SET {', '.join(updates)}"
            self.cursor.execute(executables, params)
            self.db.commit()
        except Exception as e:
            print(f"There was a problem in updating the Engineering table, problem resulted as {e}")