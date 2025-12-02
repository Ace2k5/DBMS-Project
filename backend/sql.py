"""
Main SQL database management module.

This module initializes the database connection and provides
methods to query various tables.
"""

import sqlite3
import json
from engineer import Engineer
from architect import Architect
from company import Company
from employer import Employer
from accountdb import saves
from pathlib import Path
from . import configs_backend

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
        self.db = sqlite3.connect(user_db)
        self.cursor = self.db.cursor()

        self.engineer_table = Engineer(self.db)
        self.architect_table = Architect(self.db)
        self.company_table = Company(self.db)
        self.employer_table = Employer(self.db)

    def access_user(self, name):
        lower_name = name.lower()
        base_path = Path(__file__).resolve().parent.parent
        self.save_path = base_path / "accounts_save"

        self.load_user = self.save_path / f"{lower_name}.json"

        if not self.load_user.exists():
            print(f"The user {name} does not exist.")
            return

        with open(self.load_user, "r") as f:
            data = json.load(f)

        if lower_name in data:
            db_file = data[lower_name]["db"]
            return str(self.save_path / db_file)