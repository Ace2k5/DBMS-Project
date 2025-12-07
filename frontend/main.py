import sys
from PyQt5.QtWidgets import QApplication
from frontend import account_window

def main():
    app = QApplication(sys.argv)
    window = account_window.AccountWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()