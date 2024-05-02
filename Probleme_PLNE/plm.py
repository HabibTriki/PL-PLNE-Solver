import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QFont

from gurobipy import Model, GRB

def solve_vrp(V, W, Q, C):
    N = len(Q) + 1  # Adding 1 for the depot
    m = Model("VRP")
    x = m.addVars(N, N, vtype=GRB.BINARY, name="x")
    q = m.addVars(N, vtype=GRB.CONTINUOUS, name="q")
    m.setObjective(sum(C[i][j] * x[i, j] for i in range(N) for j in range(N)), GRB.MINIMIZE)
    m.addConstrs((x.sum('*', j) == 1 for j in range(1, N)), "visit_once")
    #m.addConstr(x.sum('*' , 0) == V, "arrive_depot")
    m.addConstr(x.sum(0, '*') == V, "leave_depot")
    m.addConstrs((x[i,j] * q[i] <= W for i in range(N) for j in range(N)), "capacity")
    m.addConstrs((q[i] + Q[j-1] <= W + (1 - x[i, j]) * W for i in range(N) for j in range(1, N)), "load_continuity")
    m.optimize()

    if m.status == GRB.OPTIMAL:
        result = "Optimal Solution Found:\n"
        for i in range(N):
            for j in range(N):
                if x[i, j].x > 0.5:
                    result += f"Vehicle travels from {i} to {j}\n"
        return result
    else:
        return "No optimal solution found"

class VRPApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Vehicle Routing Problem Solver')
        layout = QVBoxLayout()


        # H1 styled heading
        heading = QLabel('Vehicle Routing Problem')
        heading.setFont(QFont('Arial', 24, QFont.Bold))  # Setting font to Arial, 24pt, bold
        layout.addWidget(heading)

        # Form layout for inputs
        formLayout = QFormLayout()
        self.numVehiclesInput = QLineEdit()
        self.capacityInput = QLineEdit()
        self.numCustomersInput = QLineEdit()
        self.demandsInput = QLineEdit()

        self.numCustomersInput.editingFinished.connect(self.setupMatrix)

        formLayout.addRow(QLabel("Number of Vehicles:"), self.numVehiclesInput)
        formLayout.addRow(QLabel("Vehicle Capacity:"), self.capacityInput)
        formLayout.addRow(QLabel("Number of Customers:"), self.numCustomersInput)
        formLayout.addRow(QLabel("Demands (comma-separated):"), self.demandsInput)

        # Table for distance matrix
        self.matrixTable = QTableWidget()
        self.matrixTable.setRowCount(1)  # Default size
        self.matrixTable.setColumnCount(1)
        layout.addLayout(formLayout)
        layout.addWidget(self.matrixTable)

        # Buttons
        self.solveButton = QPushButton('Solve VRP')
        self.solveButton.clicked.connect(self.solveProblem)
        layout.addWidget(self.solveButton)

        #Back button
        back_btn = QPushButton('Back')
        back_btn.clicked.connect(self.close)  # Close the current window
        layout.addWidget(back_btn)

        self.setLayout(layout)
        self.setGeometry(200, 200, 800, 600)

    def setupMatrix(self):
        try:
            n = int(self.numCustomersInput.text()) + 1  # Including depot
            self.matrixTable.setRowCount(n)
            self.matrixTable.setColumnCount(n)
            self.matrixTable.setHorizontalHeaderLabels([f"Node {i}" for i in range(n)])
            self.matrixTable.setVerticalHeaderLabels([f"Node {i}" for i in range(n)])
            for i in range(n):
                for j in range(n):
                    if self.matrixTable.item(i, j) is None:
                        self.matrixTable.setItem(i, j, QTableWidgetItem("0"))
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid number of customers")

    def solveProblem(self):
        try:
            V = int(self.numVehiclesInput.text())
            W = int(self.capacityInput.text())
            Q = list(map(int, self.demandsInput.text().split(',')))
            n = int(self.numCustomersInput.text()) + 1  # Including depot

            # Read matrix from table
            C = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(float(self.matrixTable.item(i, j).text()))
                C.append(row)

            result = solve_vrp(V, W, Q, C)
            QMessageBox.information(self, "Result", result)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VRPApp()
    ex.show()
    sys.exit(app.exec_())
