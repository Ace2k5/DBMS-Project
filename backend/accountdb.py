"""
This file is where the creation and deletion of accounts are.

"""
from pathlib import Path
from backend import configs_backend as configs
import json

class saves():
    def __init__(self):
        self.save_path = configs.ACCOUNT_SAVE
        self.main()
        # button.clicked.connect(self.save_account) future reference.

    def main(self):
        self.create_save_folder()
        self.load_accounts()
    
    def create_save_folder(self):
        try:
            if self.save_path.exists():
                print(f"Path already exists at {self.save_path.absolute()}")
            else:
                self.save_path.mkdir(parents=True, exist_ok=True)
                print(f"Account folder created at {self.save_path.absolute()}")

        except Exception as e:
            print(f"Something went wrong when creating the account_save files: {e}")

    def load_accounts(self):
        try:
            files = list(self.save_path.glob('*'))

            if not files:
                print("There are no available accounts in this PC.")
            else:
                print(f"There are a total of {len(files)} number of accounts in this PC.")
        except Exception as e:
            print(f"Could not load accounts using glob: {e}")

    def save_account(self, name, password):
        # if create account button is clicked (in the future) this will run)
        # 
        try:
            lower_name = name.lower()
            account_path = self.save_path / f"{lower_name}.json"
            if account_path.exists():
                print(f"Account {name} has already been created.")
                return
            
            name_db = f"{lower_name}.db"

            account = {
                lower_name: {
                    "password": password,
                    "db": name_db
                }
            }

            with open(account_path, "w") as f:
                json.dump(account, f)

            print(f"Account name {name} created.")
            return True
        except Exception as e:
            print(f"There was something wrong on save_account(): {e}")
            return False
        

    def login_account(self, name, password):
        try:
            lower_name = name.lower()
            account_path = self.save_path / f"{lower_name}.json"
            with open(account_path, "r") as f:
                data = json.load(f)

            if lower_name in data:
                if password == data[lower_name]["password"]:
                    print(f"Successfully logged in as {name}")
                    return True
        except Exception as e:
            print(f"Failed to login to account, occured as {e}")
            return False