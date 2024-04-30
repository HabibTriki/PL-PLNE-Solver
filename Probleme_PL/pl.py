import sys
from gurobipy import Model, GRB
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout

class BlendingProblemGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 700, 500)  # Adjust size as needed
        self.setWindowTitle('Blending Problem Solver')

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Title label (Heading 1)
        title_label = QLabel('Blending Problem')
        title_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        main_layout.addWidget(title_label)

        # Ingredient fields
        self.inputs = {}
        for ingredient in ['Corn', 'Wheat', 'Soy']:
            label = QLabel(f'{ingredient} (cost, protein, fat):')
            line_edit = QLineEdit()
            main_layout.addWidget(label)
            main_layout.addWidget(line_edit)
            self.inputs[ingredient] = line_edit

        # Protein and fat requirements
        self.min_protein_input = QLineEdit()
        self.max_fat_input = QLineEdit()
        main_layout.addWidget(QLabel('Minimum Protein:'))
        main_layout.addWidget(self.min_protein_input)
        main_layout.addWidget(QLabel('Maximum Fat:'))
        main_layout.addWidget(self.max_fat_input)

        # Submit button
        submit_btn = QPushButton('Solve')
        submit_btn.clicked.connect(self.solve_problem)
        main_layout.addWidget(submit_btn)

        # Result display label
        self.result_label = QLabel('')
        main_layout.addWidget(self.result_label)

        # Back button
        back_btn = QPushButton('Back')
        back_btn.clicked.connect(self.close)  # Close the current window
        main_layout.addWidget(back_btn)

    def solve_problem(self):
        # Read inputs
        cost = {}
        protein = {}
        fat = {}

        for ingredient, input_field in self.inputs.items():
            values = input_field.text().split(',')
            if len(values) == 3:
                try:
                    cost[ingredient] = float(values[0])
                    protein[ingredient] = float(values[1])
                    fat[ingredient] = float(values[2])
                except ValueError:
                    self.result_label.setText("Invalid input for one or more ingredients. Please enter numeric values.")
                    return

        try:
            min_protein = float(self.min_protein_input.text())
            max_fat = float(self.max_fat_input.text())
        except ValueError:
            self.result_label.setText("Invalid input for protein or fat requirements.")
            return

        # Initialize the model
        model = Model("Blending Problem")
        ingredients = ['Corn', 'Wheat', 'Soy']

        # Define decision variables
        amount = model.addVars(ingredients, name="amount")

        # Objective: Minimize total cost
        model.setObjective(sum(cost[i] * amount[i] for i in ingredients), GRB.MINIMIZE)

        # Constraints
        model.addConstr(sum(protein[i] * amount[i] for i in ingredients) >= min_protein, "MinProtein")
        model.addConstr(sum(fat[i] * amount[i] for i in ingredients) <= max_fat, "MaxFat")

        # Solve the model
        model.optimize()

        # Output results
        if model.status == GRB.OPTIMAL:
            result_text = "Optimal solution found:\n"
            for ingredient in ingredients:
                result_text += f"{ingredient}: {amount[ingredient].x:.2f} units\n"
            self.result_label.setText(result_text)
        else:
            self.result_label.setText("No optimal solution found.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BlendingProblemGUI()
    ex.show()
    sys.exit(app.exec_())
