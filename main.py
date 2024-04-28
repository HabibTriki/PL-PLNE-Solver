import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from Probleme_PL import pl
from Probleme_PLNE import plm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.problem_one = pl.App()
        self.problem_two = plm.VRPApp()

        self.stacked_widget.addWidget(self.problem_one)
        self.stacked_widget.addWidget(self.problem_two)

        # Navigation Buttons
        self.button1 = QPushButton('Go to Problem 1')
        self.button1.clicked.connect(self.display_problem_one)
        self.button2 = QPushButton('Go to Problem 2')
        self.button2.clicked.connect(self.display_problem_two)

        # Layout for buttons
        self.button_widget = QWidget()
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.button1)
        self.button_layout.addWidget(self.button2)
        self.button_widget.setLayout(self.button_layout)

        self.stacked_widget.addWidget(self.button_widget)
        self.stacked_widget.setCurrentWidget(self.button_widget)

    def display_problem_one(self):
        self.stacked_widget.setCurrentWidget(self.problem_one)

    def display_problem_two(self):
        self.stacked_widget.setCurrentWidget(self.problem_two)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
