from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent # double parent to go from DBMS-Project/backend/configs_backend
                                                  # to DBMS-Project
ACCOUNT_SAVE = ROOT_DIR / "accounts_save"