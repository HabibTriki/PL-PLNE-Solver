import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Probleme_PL import pl
from Probleme_PLNE import plm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Research Operation Project")
        self.setGeometry(100, 100, 800, 600)  # Adjust the size as needed

        # Central widget that contains everything
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout for the central widget
        main_layout = QVBoxLayout(central_widget)

        # Heading
        heading = QLabel('Research Operation Project:')
        heading.setFont(QFont('Arial', 24, QFont.Bold))  # Setting font to Arial, 24pt, bold
        heading.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(heading)

        # Header label with bold text
        header_label = QLabel("""Prepared by: Mohamed Habib Triki, Idris Saddi, Aymen Koched, Ala Eddine Achach""")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        main_layout.addWidget(header_label)

        # Stacked widget to switch between different problem interfaces
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.problem_one = pl.BlendingProblemGUI()
        self.problem_two = plm.VRPApp()

        self.stacked_widget.addWidget(self.problem_one)
        self.stacked_widget.addWidget(self.problem_two)

        # Navigation Buttons
        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button1 = QPushButton('Go to Problem 1')
        button1.clicked.connect(self.display_problem_one)
        button2 = QPushButton('Go to Problem 2')
        button2.clicked.connect(self.display_problem_two)
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.stacked_widget.addWidget(button_widget)
        self.stacked_widget.setCurrentWidget(button_widget)

    def display_problem_one(self):
        self.stacked_widget.setCurrentWidget(self.problem_one)

    def display_problem_two(self):
        self.stacked_widget.setCurrentWidget(self.problem_two)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
