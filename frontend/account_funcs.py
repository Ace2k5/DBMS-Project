from PyQt5.QtWidgets import QLineEdit, QPushButton
from backend import accountdb

class AccountFunctionality():
    def __init__(self, username: QLineEdit, password: QLineEdit, login_btn: QPushButton, signup_btn: QPushButton):
        self.saves = accountdb.saves()
        self.username = username
        self.password = password
        self.login_btn = login_btn
        self.signup_btn = signup_btn

        self.connect_buttons()

    def connect_buttons(self):
        self.signup_btn.clicked.connect(lambda: self.saves.save_account(self.username.text(), self.password.text()))
        self.login_btn.clicked.connect(lambda: self.saves.login_account(self.username.text(), self.password.text()))


