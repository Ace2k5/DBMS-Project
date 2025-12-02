from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QLineEdit,
                             QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout)
from pathlib import Path
from . import utils_frontend as utils
from . import configs_frontend as configs
from . import qt_painter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupCentralWidget()
        self.setupMainWindow()
        self.setupQtWidgets()

    def background(self):
        base_path = Path(__file__).resolve().parent
        building_bg = base_path.parent / "imgs" / "buildings_bg.jpg"
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

        self.main_layout.addStretch()

        name = QLabel()
        name.setText(configs.pyqt["application_name"])
        name.setStyleSheet("""font-size: 32px;
                           font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 10px;
                            background-color: rgba(0, 0, 0, 50);
                           """)
        name.setAlignment(Qt.AlignCenter)
        
        username = QLineEdit()
        username.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        username.setFixedWidth(200)

        password = QLineEdit()
        password.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        password.setFixedWidth(200)

        login = QPushButton()
        login.setText("Login")
        login.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        
        sign_up = QPushButton()
        sign_up.setText("Sign in")
        sign_up.setStyleSheet("""
                            font-size: 16px;
                            font-family: Times New Roman;
                            font-weight: bold;
                            color: white;
                            padding: 1px;
                            border: 1px solid white;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 50);
                            """)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(login, 0, alignment=Qt.AlignCenter)
        hbox.addWidget(sign_up, 0, alignment=Qt.AlignCenter)
        hbox.addStretch()

        self.main_layout.addWidget(name, 0, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(username, 0, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(password, 0 ,alignment=Qt.AlignCenter)
        self.main_layout.addLayout(hbox)
        self.main_layout.addStretch()