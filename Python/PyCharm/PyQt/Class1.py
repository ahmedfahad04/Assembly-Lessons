from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit


class OurMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Class 1: Create your 1st Qt Window")
        self.setMinimumSize(500,500)
        self.setMaximumSize(600,600)

        btn = QPushButton("Click Here")

        self.setCentralWidget(btn)


app = QApplication([])
window = OurMainWindow()
window.show()

app.exec()
