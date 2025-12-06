from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout,
                             QComboBox, QTableWidget, QHeaderView, QTableWidgetItem, QStyleFactory,
                             QListView)
from pathlib import Path
from . import configs_frontend as configs, utils_frontend as utils, project_management_funcs
import sqlite3

class ProjectWindow(QMainWindow):
    def __init__(self, db: sqlite3):
        super().__init__()
        self.db_manager = db # self.save_data / username
        self.setupMainWindow()
        self.setupQt()

        self.funcs = project_management_funcs.ProjectFunctions(self, self.db_manager)

    def setupMainWindow(self):
        window_width, window_height = configs.pyqt["resolution"]
        middle_of_screen = utils.coordinates_middle(window_width, window_height)
        self.setGeometry(middle_of_screen[0], middle_of_screen[1], window_width, window_height)
        self.setWindowTitle(configs.pyqt["application_name"])
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
                            QTableWidget { 
                                background-color: #1e1e1e; 
                                gridline-color: #333; 
                                border: 1px solid #555; 
                            }
                            QHeaderView::section {
                                background-color: #3e3e42;
                                padding: 4px;
                                border: 1px solid #555;
                            }
                           """)

    def setupQt(self):
        self.widget = QWidget()
        self.main_layout = QHBoxLayout(self.widget)
        self.main_layout.setContentsMargins(5,5,5,5)
        self.main_layout.setSpacing(10)
        self.setCentralWidget(self.widget)

        #outer vbox
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()

        #vbox 1
        self.project_assignment_btn = self.generic_btn("Project Assignment")
        self.project_btn, self.combo_project = self.generic_btn("Project", ["All", "Budget", "Assigned People", "Company"])
        self.company_btn, self.combo_company = self.generic_btn("Company", ["All", "Phone Number", "Email", "Address", "Date of Request"])
        self.person_btn, self.combo_person = self.generic_btn("Hired People", ["All", "Phone Number", "Email", "Role", "Hiring Date"])

        self.vbox1.addWidget(self.project_assignment_btn)

        self.vbox1.addWidget(self.project_btn)
        self.vbox1.addWidget(self.combo_project)
        self.vbox1.addSpacing(5)

        self.vbox1.addWidget(self.company_btn)
        self.vbox1.addWidget(self.combo_company)
        self.vbox1.addSpacing(5)

        self.vbox1.addWidget(self.person_btn)
        self.vbox1.addWidget(self.combo_person)
        self.vbox1.addSpacing(5)

        self.vbox1.addStretch()

        # vbox 2
        self.table = QTableWidget()
        self.table.setStyleSheet("background-color: #1e1e1e; gridline-color: #555;")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.innerhbox = QHBoxLayout()
        self.create_btn = QPushButton("Create")
        self.update_btn = QPushButton("Update")
        self.delete_btn = QPushButton("Destroy")

        self.innerhbox.addWidget(self.create_btn)
        self.innerhbox.addWidget(self.update_btn)
        self.innerhbox.addWidget(self.delete_btn)
        

        self.vbox2.addWidget(self.table)
        self.vbox2.addLayout(self.innerhbox)

        self.main_layout.addLayout(self.vbox1, 1)
        self.main_layout.addLayout(self.vbox2, 3)
    
    def generic_btn(self, text: str, combo: list=None):
        if combo is None:
            btn = QPushButton(text)
            return btn
        else:
            btn = QPushButton(text)
            combobox = QComboBox()
            combobox.addItems(combo)
            combobox.setEditable(False)
            combobox.setStyle(QStyleFactory.create("Fusion"))
            combobox.setView(QListView())
            return btn, combobox

