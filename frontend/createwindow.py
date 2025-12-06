from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout,
                             QComboBox, QTableWidget, QHeaderView, QTableWidgetItem, QStyleFactory,
                             QListView)
from pathlib import Path
from . import configs_frontend as configs, utils_frontend as utils, project_management_funcs
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