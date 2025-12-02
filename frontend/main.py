import sys
from PyQt5.QtWidgets import QApplication
from . import main_window

def main():
    app = QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()