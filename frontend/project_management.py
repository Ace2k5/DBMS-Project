from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout)
from pathlib import Path
from . import configs_frontend as configs, utils_frontend as utils

class ProjectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupMainWindow()

    def setupMainWindow(self):
        window_width, window_height = configs.pyqt["resolution"]
        middle_of_screen = utils.coordinates_middle(window_width, window_height)
        self.setGeometry(middle_of_screen[0], middle_of_screen[1], window_width, window_height)
        self.setWindowTitle(configs.pyqt["application_name"])