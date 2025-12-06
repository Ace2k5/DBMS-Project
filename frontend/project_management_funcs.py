from PyQt5.QtWidgets import QTableWidgetItem
from backend.company import Company
from backend.person import Person
from backend.project import Project
from backend.project_assignment import ProjectAssignment

class ProjectFunctions():
    def __init__(self, main_window, db_manager):
        self.mw = main_window
        self.manager = db_manager

        # Initialize Backend Tables
        self.company_table = self.manager.company_table
        self.person_table = self.manager.person_table
        self.project_table = self.manager.project
        self.assignment_table = self.manager.project_assignment

        self.connect_buttons()

    def connect_buttons(self):
        self.mw.project_assignment_btn.clicked.connect(self.display_assigned_projects)
        self.mw.company_btn.clicked.connect(self.display_companies)
        self.mw.person_btn.clicked.connect(self.display_people)
        self.mw.project_btn.clicked.connect(self.display_projects)

    def display_assigned_projects(self):
        headers = ["ID", "Company ID", "Project ID", "Person ID", "Status"]
        self.mw.table.setColumnCount(len(headers))
        self.mw.table.setHorizontalHeaderLabels(headers)

        data = self.assignment_table.select()

        self.fill_table(data)

    def display_companies(self):
        current_text = self.mw.combo_company.currentText()

        column_mapping = {
            "Phone Number": "Phone_Number",
            "Email": "Email",
            "Address": "Address",
            "Date of Request": "Date_of_Request"
        }

        if current_text == "All":
            headers = ["ID", "Name", "Phone", "Email", "Address", "Date"]
            self.mw.table.setColumnCount(len(headers))
            self.mw.table.setHorizontalHeaderLabels(headers)
            db_column = []
        else:
            headers = ["ID", "Name", current_text]
            self.mw.table.setColumnCount(len(headers))
            self.mw.table.setHorizontalHeaderLabels(headers)

            db_column = ["Company_ID", "Company_Name", column_mapping.get(current_text)]

        data = self.company_table.select(*db_column)

        self.fill_table(data)

    def display_people(self):
        current_text = self.mw.combo_person.currentText()
        column_mapping = {
            "Phone Number": "Phone_Number",
            "Email": "Email",
            "Role": "Role",
            "Hiring Date": "Hiring_Date",
        }

        if current_text == "All":
            headers = ["ID", "Name", "Phone", "Email", "Role", "Hiring Date"]
            self.mw.table.setColumnCount(len(headers))
            self.mw.table.setHorizontalHeaderLabels(headers)

            db_column = []
        else:
            headers = ["ID", "Name", current_text]
            self.mw.table.setColumnCount(len(headers))
            self.mw.table.setHorizontalHeaderLabels(headers)

            db_column = ["Person_ID", "Name", column_mapping.get(current_text)]

        data = self.person_table.select(*db_column)
        self.fill_table(data)

    def display_projects(self):
        headers = ["ID", "Name", "Budget"]
        self.mw.table.setColumnCount(len(headers))
        self.mw.table.setHorizontalHeaderLabels(headers)

        data = self.project_table.select()
        self.fill_table(data)

    def fill_table(self, data):
        """Helper function to fill the table widget with list data"""
        self.mw.table.setRowCount(0)
        
        if not data:
            return

        self.mw.table.setRowCount(len(data))
        
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                cell_item = QTableWidgetItem(str(item)) 
                self.mw.table.setItem(row_idx, col_idx, cell_item)