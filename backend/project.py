'''

The purpose of this file is to create the project using engineer, architect, company and employer as foreign keys.

'''

import sqlite3
from architect import Architect
from company import Company
from engineer import Engineer
from employer import Employer

class Project():
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.cursor = self.db.cursor()
        
    def create_project_table(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Project(
                    Project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Project_Name TEXT,
                    Budget TEXT,
                    Company_ID INTEGER,
                    Employer_ID INTEGER,
                    Engineer_ID INTEGER,
                    Architect_ID INTEGER,
                    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID),
                    FOREIGN KEY (Employer_ID) REFERENCES Employer(Employer_ID),
                    FOREIGN KEY (Engineer_ID) REFERENCES Engineer(Engineer_ID),
                    FOREIGN KEY (Architect_ID) REFERENCES Architect(Architect_ID),
                    Is_Done TEXT
                )
                """
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not create the projects table, occured as {e}")
            
    def insert_project_value(self, name: str, budget: str, company: int, employer: int, engineer: int, architect: int, is_done: str):
        try:
            self.cursor.execute(
                """
                INSERT INTO Project(Project_Name, Budget, Company_ID, Employer_ID, Engineer_ID, Architect_ID, Is_Done) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name, budget, company, employer, engineer, architect, is_done)
            )
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"Could not insert values into project,")
            
    def update_project_value(self, project_id: int=None, name: str=None, budget: str=None, company: int=None, employer: int=None, engineer: int=None, architect: int=None, is_done: str=None):
        
        try:
            updates = []
            params = []
            
            if name is not None:
                updates.append("Project_Name = ?")
                params.append(name)
            if budget is not None:
                updates.append("Budget = ?")
                params.append(budget)
            if company is not None:
                updates.append("Company_ID = ?")
                params.append(company)
            if employer is not None:
                updates.append("Employer_ID = ?")
                params.append(employer)
            if engineer is not None:
                updates.append("Engineer_ID = ?")
                params.append(engineer)
            if architect is not None:
                updates.append("Architect_ID = ?")
                params.append(architect)
            if is_done is not None:
                updates.append("Is_Done = ?")
                params.append(is_done)
            
            if not updates:
                print("There was nothing to update, no given parameters. Returning...")
                return
            
            params.append(project_id)
            
            query = f"UPDATE Project SET {', '.join(updates)} WHERE Project_ID = ?"
            self.cursor.execute(query, params)
            self.db.commit()
            print(f"Successfully updated Engineer ID: {project_id}")
        except Exception as e:
            print(f"Could not update Project table, occured as {e}")
    
    def delete_id(self, project_id: int):
        '''
        This function aims to remove an engineer row based on the id
        '''
        try:
            self.cursor.execute(
                "DELETE FROM Project WHERE Project_ID = ?", (project_id,) 
            )
            self.db.commit()
        except Exception as e:
            print(f"Could not delete project row, occured as {e}")
        