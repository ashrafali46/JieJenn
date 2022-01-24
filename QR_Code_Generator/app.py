import os
import sys
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QWidget, QApplication


class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 550)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())
