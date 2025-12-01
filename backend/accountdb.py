"""
This file is where the creation and deletion of accounts are.

"""
from pathlib import Path
import json

class saves():
    def __init__(self):
        self.save_path = Path("../account_saves")
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
            account_path = self.save_path / f"{name.lower()}.json"
            if account_path.exists():
                print(f"Account {name} has already been created.")
                return
            
            account = {
                name: password
            }

            with open(account_path, "w") as f:
                json.dump(account, f)

            print(f"Account name {name} created.")
        except Exception as e:
            print(f"There was something wrong on save_account(): {e}")    