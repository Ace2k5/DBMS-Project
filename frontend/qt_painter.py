from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap, QColor

class Painter(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.bg_pixmap = QPixmap(self.image_path)

    def paintEvent(self, event):
        painter = QPainter(self)

        pixmap = QPixmap(self.image_path)

        target_rect = self.rect()
        painter.drawPixmap(target_rect, pixmap)
        painter.fillRect(target_rect, QColor(0, 0, 0, 150))