import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QVBoxLayout, QGridLayout, QGroupBox, QApplication)
import sqlite3

# Mocking your config imports for this standalone example
# You can uncomment your original imports
# from frontend import configs_frontend as configs, utils_frontend as utils

class CreateWindow(QMainWindow):
    def __init__(self, db: sqlite3.Connection = None):
        super().__init__()
        self.setWindowTitle("Project Management")
        self.resize(1000, 700) # Default size
        self.setupQt()

    def setupQt(self):
        self.widget = QWidget()
        self.main_layout = QVBoxLayout(self.widget)
        # Add some spacing around the edges
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        
        self.setCentralWidget(self.widget)
        
        # --- MODERN STYLESHEET ---
        self.setStyleSheet("""
            QMainWindow {
                background-color: #212121;
            }
            QWidget {
                color: #e0e0e0;
                font-family: "Segoe UI", "Roboto", "Helvetica", sans-serif;
                font-size: 14px;
            }
            /* Group Box Styling */
            QGroupBox {
                border: 1px solid #3e3e42;
                border-radius: 6px;
                margin-top: 12px;
                padding-top: 10px;
                font-weight: bold;
                font-size: 15px;
                color: #4da6ff; /* Accent color for titles */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            /* Input Styling */
            QLineEdit {
                background-color: #2b2b2f; /* Darker input background */
                border: 1px solid #3e3e42;
                border-radius: 4px;
                padding: 6px;
                color: white;
                selection-background-color: #4da6ff;
            }
            QLineEdit:focus {
                border: 1px solid #4da6ff; /* Highlight on focus */
                background-color: #333336;
            }
            /* Label Styling */
            QLabel {
                color: #b0b0b0; /* Softer text color for labels */
                font-weight: normal;
            }
            /* Header Label */
            QLabel#Header {
                font-size: 22px;
                font-weight: bold;
                color: white;
                margin-bottom: 10px;
            }
        """)

        # Main Header
        header = QLabel("Create New Entry")
        header.setObjectName("Header")
        self.main_layout.addWidget(header, alignment=Qt.AlignHCenter)

        # 1. Project Assignment Section
        self.create_section("Project Assignment", [
            ("Company ID:", "txt_company_id"), 
            ("Project ID:", "txt_project_id"), 
            ("Person ID:", "txt_person_id")
        ])

        # 2. Project Details Section
        self.create_section("Project Details", [
            ("Name:", "txt_proj_name"), 
            ("Budget:", "txt_budget")
        ])

        # 3. Company Section
        self.create_section("Company Information", [
            ("Company Name:", "txt_comp_name"), 
            ("Phone Number:", "txt_comp_phone"),
            ("Email:", "txt_comp_email"),
            ("Address:", "txt_address"),
            ("Date of Request:", "txt_date_req")
        ])

        # 4. Person Section
        self.create_section("Person Information", [
            ("Name:", "txt_pers_name"),
            ("Phone Number:", "txt_pers_phone"),
            ("Email:", "txt_pers_email"),
            ("Role:", "txt_role"),
            ("Hiring Date:", "txt_hiring_date")
        ])

        # Add a spacer at the bottom to push everything up
        self.main_layout.addStretch()

    def create_section(self, title, fields):
        """
        Creates a GroupBox with a Grid Layout for the fields.
        fields: list of tuples [("Label Text", "ObjectName")]
        """
        group = QGroupBox(title)
        grid = QGridLayout()
        # Spacing between items in the grid
        grid.setVerticalSpacing(15) 
        grid.setHorizontalSpacing(15)

        # Logic to arrange items in columns (e.g., 3 pairs per row)
        cols_per_row = 3
        
        for i, (label_text, obj_name) in enumerate(fields):
            row = i // cols_per_row
            col = (i % cols_per_row) * 2 # Multiply by 2 because Label+Input = 2 slots

            lbl = QLabel(label_text)
            inp = QLineEdit()
            inp.setObjectName(obj_name) # Useful for getting values later

            grid.addWidget(lbl, row, col)
            grid.addWidget(inp, row, col + 1)

        group.setLayout(grid)
        self.main_layout.addWidget(group)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateWindow()
    window.show()
    sys.exit(app.exec_())