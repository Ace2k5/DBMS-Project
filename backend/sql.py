import sqlite3
from engineer import Engineer

class SQL():        
    def init(self):
        '''
        This class will aim to initialize the SQL connection so that the tables can use it
        '''
        self.db = sqlite3.connect(":memory:")
        self.engineer_table = Engineer(self.db)
        