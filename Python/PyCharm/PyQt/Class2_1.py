from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QLabel, QVBoxLayout


class OurMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal and Slots Practice")

        self.label = QLabel("IIT")

        self.clrbtn = QPushButton("Clear")
        self.savebtn = QPushButton("Save")

        self.myinput = QLineEdit("Enter your Name: ")
        self.myinput.textChanged.connect(self.label.setText)
        self.clrbtn.clicked.connect(self.label.clear)
        self.clrbtn.clicked.connect(self.myinput.clear)
        self.savebtn.clicked.connect(self.save_the_label)

        layout = QVBoxLayout()
        layout.addWidget(self.myinput)
        layout.addWidget(self.label)
        layout.addWidget(self.clrbtn)
        layout.addWidget(self.savebtn)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container) # important!!!

    def save_the_label(self):
        with open("demo.txt", "w") as f:
            f.write(self.label.text())

        f.close()


app = QApplication([])

window = OurMainWindow()
window.show()

app.exec()

