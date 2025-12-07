"""
Main SQL database management module.

This module initializes the database connection and provides
methods to query various tables.
"""

import sqlite3
import json
from backend.company import Company
from backend.person import Person
from backend.project import Project
from backend.project_assignment import ProjectAssignment
from backend.accountdb import saves
from pathlib import Path
from backend import configs_backend as configs

class SQLDatabaseManager():        
    def __init__(self):
        """
        Initialize the SQL database connection and create table instances.
        """
        self.accountdb = saves()

    def create_db(self, name):
        """
        Initialize the SQL database connection and create table instances.
        """
        user_db = self.access_user(name)
        if not user_db:
            print("Failted to get the database path")
            return False
        self.db = sqlite3.connect(user_db)
        self.cursor = self.db.cursor()
        self.db.execute("PRAGMA foreign_keys = ON")

        self.company_table = Company(self.db, self.cursor)
        self.person_table = Person(self.db, self.cursor)
        self.project = Project(self.db, self.cursor)
        self.project_assignment = ProjectAssignment(self.db, self.cursor)

        try:
            self.company_table.create_table()
            self.person_table.create_table()
            self.project.create_table()
            self.project_assignment.create_table()
            print("All tables created successfully")
            return self.db
        except Exception as e:
            print(f"Failed to create tables: {e}")
            return None

    def access_user(self, name) -> str | None:
        try:
            if name is None:
                print("No name given.")
                return None
            lower_name = name.lower()
            self.save_path = configs.ACCOUNT_SAVE
            self.save_path.mkdir(parents=True, exist_ok=True)

            self.load_user = self.save_path / f"{lower_name}.json"
            if not self.load_user.exists():
                print(f"The user {name} does not exist. Creating new SQL database file...")
                file = f"{name}.db"
                return str(self.save_path/file)

            with open(self.load_user, "r") as f:
                data = json.load(f)

            if lower_name in data:
                db_file = data[lower_name]["db"]
                return str(self.save_path / db_file)
        except Exception as e:
            print(f"Accessing the user failed, {e}")