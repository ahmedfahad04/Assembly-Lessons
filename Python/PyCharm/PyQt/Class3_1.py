import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Exploration")

        label = QLabel("Istiaq Ahmed Fahad")

        font = label.font()
        font.setPointSize(30)
        font.setItalic(True)
        font.setBold(True)
        font.setFamily("Algerian")
        font.setCapitalization(True)

        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label.setPixmap(QPixmap("compare.png"))
        label.setScaledContents(True)

        self.setCentralWidget(label)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
