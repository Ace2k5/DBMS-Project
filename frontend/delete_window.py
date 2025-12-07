from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QVBoxLayout, QComboBox, QMessageBox)
from frontend import configs_frontend as configs, utils_frontend as utils

class DeleteWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setupMainWindow()
        self.setupQt()

    def setupMainWindow(self):
        # Using popups_resolution from your config
        window_width, window_height = configs.pyqt["popups_resolution"]
        middle_of_screen = utils.coordinates_middle(window_width, window_height)
        self.setGeometry(middle_of_screen[0], middle_of_screen[1], window_width, window_height)
        self.setWindowTitle("Delete Entry")

    def setupQt(self):
        self.widget = QWidget()
        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(self.widget)