from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout)
from pathlib import Path
from . import configs_frontend as configs, utils_frontend as utils, qt_painter, account_funcs

class AccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupCentralWidget()
        self.setupMainWindow()
        self.setupQtWidgets()

        account_funcs.AccountFunctionality(self.username, self.password, self.login, self.sign_up)

    def background(self):
        base_path = configs.IMG_DIR
        building_bg = base_path / "buildings_bg.jpg"
        print(f"Looking for image at: {building_bg}")
        return str(building_bg)

    def setupMainWindow(self):
        window_width, window_height = configs.pyqt["resolution"]
        middle_of_screen = utils.coordinates_middle(window_width, window_height)
        self.setGeometry(middle_of_screen[0], middle_of_screen[1], window_width, window_height)
        self.setWindowTitle(configs.pyqt["application_name"])

    def setupCentralWidget(self):
        self.widget = qt_painter.Painter(self.background())
        self.main_layout = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)

    def setupQtWidgets(self):

        self.saved_buttons = []

        self.main_layout.addStretch()

        self.name = QLabel()
        self.name.setText(configs.pyqt["application_name"])
        self.name.setStyleSheet("""font-size: 32px;
                           font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 10px;
                            background-color: rgba(0, 0, 0, 50);
                           """)
        self.name.setAlignment(Qt.AlignCenter)
        
        self.username = QLineEdit()
        self.username.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        self.username.setFixedWidth(200)

        self.password = QLineEdit()
        self.password.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        self.password.setFixedWidth(200)

        self.login = QPushButton()
        self.login.setText("Login")
        self.login.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        
        self.sign_up = QPushButton()
        self.sign_up.setText("Sign in")
        self.sign_up.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        
        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.login, 0, alignment=Qt.AlignCenter)
        self.hbox.addWidget(self.sign_up, 0, alignment=Qt.AlignCenter)
        self.hbox.addStretch()

        self.main_layout.addWidget(self.name, 0, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.username, 0, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.password, 0 ,alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.hbox)
        self.main_layout.addStretch()