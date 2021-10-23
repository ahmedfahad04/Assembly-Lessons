from random import choice

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit

list_of_window_title = [
    'My App',
    'My App',
]


class OurMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Class 2: Signals and Slots")

        self.button = QPushButton("Click Here")
        self.button.clicked.connect(self.button_was_clicked)  # signal
        self.windowTitleChanged.connect(self.the_window_title_was_changed)  # signal

        self.setCentralWidget(self.button)  # most important!!

    def button_was_clicked(self, checked):  # slot method
        print("Clicked")

        new_window_title = choice(list_of_window_title)
        print("New Window Title: ", new_window_title, "Checked: ", checked)

        self.setWindowTitle(new_window_title)  # then goto 19th line

    def the_window_title_was_changed(self, new_title):  # slot method
        print("Changed Window Title is ", new_title)

        # if new_title == "My App":
        #     self.button.setDisabled(True)
        #     return


app = QApplication([])
window = OurMainWindow()
window.show()

app.exec()
