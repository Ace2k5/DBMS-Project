from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout,
                             QComboBox, QTableWidget, QHeaderView, QTableWidgetItem, QStyleFactory,
                             QListView)
from pathlib import Path
from frontend import configs_frontend as configs, utils_frontend as utils, project_management_funcs
import sqlite3

class CreateWindow(QMainWindow):
    def __init__(self, db: sqlite3.Connection):
        super().__init__()
        self.setupMainWindow()
        self.setupQt()

    def setupMainWindow(self):
        window_width, window_height = configs.pyqt["popups_resolution"]
        middle_of_screen = utils.coordinates_middle(window_width, window_height)
        self.setGeometry(middle_of_screen[0], middle_of_screen[1], window_width, window_height)
        self.setWindowTitle(configs.pyqt["application_name"])

    def setupQt(self):
        self.widget = QWidget()
        self.main_layout = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)
        self.setStyleSheet("""
                           QMainWindow {background-color: #2b2b2f; color: white;}
                           QWidget { color: white; font-size: 14px; }
                           QPushButton { 
                            background-color: #3e3e42; 
                            border: 1px solid #555; 
                            padding: 8px; 
                            border-radius: 4px;
                            min-height: 20px;
                            }
                            QPushButton:hover { background-color: #505055; }
                            QPushButton:pressed { background-color: rgba(30, 30, 30, 0.5); }
                            QComboBox {
                                background-color: #1e1e1e;
                                color: white;
                                border: 1px solid rgba(85, 85, 85, 0.25);
                                padding: 5px;
                            }
                            QComboBox QAbstractItemView {
                                background-color: #1e1e1e;
                                color: white;
                                outline: 0;
                            }
                           QComboBox QAbstractItemView::item:selected {
                                background-color: rgba(30, 30, 30, 0.5);
                                color: white;
                            }
                           
                           QComboBox QAbstractItemView::item:hover {
                                background-color: rgba(60, 60, 60, 0.5);
                                color: white;
                            }
                            QLabel {
                                font-size: 16px;
                                font-family: Times New Roman;
                                font-weight: bold;
                                color: white;
                                padding: 10px;
                           }
                           """)
        label = QLabel()
        label.setText("Create")

        self.main_layout.addWidget(label, alignment=Qt.AlignHCenter)

        pa_label = QLabel()
        pa_label.setText("Project Assignment")
        pa_label.setStyleSheet("background-color: rgba(0, 0, 0, 50);")
        self.hbox1 = QHBoxLayout()
        #project assignment
        company_id_label, project_id_label, person_id_label = (QLabel(n) for n in ["Company ID:", "Project ID:", "Person ID:"])
        company_id_input, project_id_input, person_id_input = (QLineEdit() for _ in range(3))
        self.add_widgets(self.hbox1, company_id_label, company_id_input, project_id_label, project_id_input,
                         person_id_label, person_id_input)

        self.hbox2 = QHBoxLayout()
        #project
        name_label, budget_label, project_label = (QLabel(n) for n in ["Name:", "Budget:", "Project"])
        name_input, budget_input = (QLineEdit() for _ in range(2))
        self.add_widgets(self.hbox2, name_label, name_input, budget_label, budget_input)
        self.hbox3 = QHBoxLayout()
        #company
        company_name_label, company_phone_label, company_email_label, address_label, date_request_label, company_label = (QLabel(n) for n in ["Company Name:", "Phone Number:", "Email: ", "Address", "Date of Request:", "Company"])
        company_name_input, company_phone_input, company_email_input, address_input, date_request_input = (QLineEdit() for _ in range(5))
        self.add_widgets(self.hbox3, company_name_label, company_name_input, company_email_label, company_email_input, company_phone_label, company_phone_input, address_label, address_input, date_request_label, date_request_input)
        self.hbox4= QHBoxLayout()
        #person
        person_name_label, person_phone_label, person_email_label, role_label, hiring_date_label, person_label = (QLabel(n) for n in ["Name:", "Phone Number:", "Email:", "Role:", "Hiring Date:", "Person"])
        person_name_input, person_phone_input, person_email_input, role_input, hiring_date_input = (QLineEdit() for _ in range(5))
        self.add_widgets(self.hbox4, person_name_label, person_name_input, person_phone_label, person_phone_input, person_email_label, person_email_input, role_label, role_input, hiring_date_label, hiring_date_input)

        list_pair = [(pa_label, self.hbox1), (project_label, self.hbox2), (company_label, self.hbox3), (person_label, self.hbox4)]
        self.main_layout_helper(list_pair)
                                   

    def main_layout_helper(self, list_pair:list):
        for label, layout in list_pair:
            self.main_layout.addWidget(label, alignment=Qt.AlignHCenter)
            self.main_layout.addLayout(layout)

    def add_widgets(self, box, *widget):
        for widg in widget:
            box.addWidget(widg)