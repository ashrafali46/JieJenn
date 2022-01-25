import os
import sys
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStatusBar


class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 550)
        self.setWindowTitle('QR Code Generator')

        self.initUI()

    def initUI(self):
        font = QFont('Open Sans', 16)

        mainLayout = QVBoxLayout()
        entryLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        imageLayout = QVBoxLayout()
        imageLayout.addStretch()

        label = QLabel('Enter Text:')
        label.setFont(font)

        self.textEntry = QLineEdit()
        self.textEntry.setFont(font)

        entryLayout.addWidget(label)
        entryLayout.addWidget(self.textEntry)

        mainLayout.addLayout(entryLayout)

        self.buttonGenerate = QPushButton('Generate QR Code')
        self.buttonGenerate.clicked.connect(self.create_qr_code)

        self.buttonSaveImage = QPushButton('Save QR Image')
        self.buttonSaveImage.clicked.connect(self.save_qr_code)

        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(self.clear_fields)

        buttonLayout.addWidget(self.buttonGenerate)
        buttonLayout.addWidget(self.buttonSaveImage)
        buttonLayout.addWidget(self.buttonClear)
        mainLayout.addLayout(buttonLayout)

        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        imageLayout.addWidget(self.imageLabel)
        mainLayout.addLayout(imageLayout)

        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar)

        self.setLayout(mainLayout)

    def clear_fields(self):
        self.textEntry.clear()
        self.imageLabel.clear()
        self.statusBar.clearMessage()

    def create_qr_code(self):
        text = self.textEntry.text()
        img = qrcode.make(text)
        qr = ImageQt(img)
        pix = QPixmap.fromImage(qr)
        self.imageLabel.setPixmap(pix)

    def save_qr_code(self):
        current_dir = os.getcwd()
        file_name = self.textEntry.text()

        if file_name:
            self.imageLabel.pixmap().save(os.path.join(current_dir, file_name + '.png'))
            self.statusBar.showMessage(f'Image it saved at {os.path.join(current_dir, file_name + ".png")}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QPushButton {height: 50px; font-size: 24px;}')
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())
