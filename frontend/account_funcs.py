from PyQt5.QtWidgets import QLineEdit, QPushButton
from backend import accountdb

class AccountFunctionality():
    def __init__(self, account_buttons: list[QLineEdit, QLineEdit, QPushButton, QPushButton]):
        self.saves = accountdb.saves()

        self.account_buttons = account_buttons
        self.get_text()

    def get_text(self):
        self.username, self.password = self.account_buttons[0].text(), self.account_buttons[1].text()

    def connect_buttons(self):
