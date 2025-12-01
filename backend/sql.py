"""
Main SQL database management module.

This module initializes the database connection and provides
methods to query various tables.
"""

import sqlite3
from engineer import Engineer
from accountdb import saves
from pathlib import Path

class SQLDatabaseManager():        
    def __init__(self):
        """
        Initialize the SQL database connection and create table instances.
        
        Uses an in-memory SQLite database for temporary storage.
        """
        self.accountdb = saves()
        self.account_path = Path("../account_saves")
        self.temp_account = self.accountdb.save_account("L", "123")
        self.create_db("L")

    def create_db(self, name):
        """
        Initialize the SQL database connection and create table instances.
        """
        local_account_path = self.account_path / f"{name}.db"
        self.db = sqlite3.connect(local_account_path)
        self.cursor = self.db.cursor()
        self.engineer_table = Engineer(self.db)