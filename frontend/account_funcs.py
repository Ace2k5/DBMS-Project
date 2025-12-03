from PyQt5.QtWidgets import QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
from backend import accountdb

class AccountFunctionality(QObject):
    login_success = pyqtSignal()
    signup_success = pyqtSignal()
    def __init__(self, username: QLineEdit, password: QLineEdit, login_btn: QPushButton, signup_btn: QPushButton):
        super().__init__()
        self.saves = accountdb.saves()
        self.username = username
        self.password = password
        self.login_btn = login_btn
        self.signup_btn = signup_btn

        self.connect_buttons()

    def connect_buttons(self):
        self.signup_btn.clicked.connect(self.save_account)
        self.login_btn.clicked.connect(self.load_account)

    def save_account(self):
        success = self.saves.save_account(self.username.text(), self.password.text())
        if success:
            self.signup_success.emit()
    
    def load_account(self):
        success = self.saves.login_account(self.username.text(), self.password.text())
        if success:
            self.login_success.emit()


        
