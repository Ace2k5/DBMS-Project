import sqlite3
from engineer import Engineer

class SQL():        
    def __init__(self):
        '''
        This class will aim to initialize the SQL connection so that the tables can use it
        '''
        self.db = sqlite3.connect(":memory:")
        self.cursor = self.db.cursor()
        self.engineer_table = Engineer(self.db)
    
    def show_engineer_table(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Engineer
                """
            )
        except Exception as e:
            print(f"Failed in getting the values from Engineer table, occured as {e}")
        
    def show_company_table(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Company
                """
            )
        except Exception as e:
            print(f"Failed in getting the values from Company table, occured as {e}")
            
    def show_company_table(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Employer
                """
            )
        except Exception as e:
            print(f"Failed in getting the values from Employer table, occured as {e}")