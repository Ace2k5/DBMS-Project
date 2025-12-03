from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent # double parent to go from DBMS-Project/backend/configs_backend
                                                  # to DBMS-Project
IMG_DIR = ROOT_DIR / "imgs"
pyqt = {
    "application_name": "Sect | Project Management",
    "resolution" : (1000, 500)
}