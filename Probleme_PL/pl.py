import sys
from gurobipy import Model, GRB
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout

class BlendingProblemGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ingredients = []
        self.constraints = {}
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
        self.input_layout = QVBoxLayout()
        main_layout.addLayout(self.input_layout)
        self.add_ingredient_field()

        # Constraint fields
        self.constraint_layout = QVBoxLayout()
        main_layout.addLayout(self.constraint_layout)
        self.add_constraint_field()

        # Add ingredient button
        add_ingredient_btn = QPushButton('Add Ingredient')
        add_ingredient_btn.clicked.connect(self.add_ingredient_field)
        main_layout.addWidget(add_ingredient_btn)

        # Add constraint button
        add_constraint_btn = QPushButton('Add Constraint')
        add_constraint_btn.clicked.connect(self.add_constraint_field)
        main_layout.addWidget(add_constraint_btn)

        # Submit button
        submit_btn = QPushButton('Solve')
        submit_btn.clicked.connect(self.solve_problem)
        main_layout.addWidget(submit_btn)

        # Result display label
        self.result_label = QLabel('')
        main_layout.addWidget(self.result_label)

        # Back button
        back_btn = QPushButton('Back')
        back_btn.clicked.connect(self.close)
        main_layout.addWidget(back_btn)

    def add_ingredient_field(self):
        ingredient_layout = QVBoxLayout()
        self.input_layout.addLayout(ingredient_layout)

        ingredient_label = QLabel('Ingredient (name, cost):')
        ingredient_layout.addWidget(ingredient_label)

        ingredient_line_edit = QLineEdit()
        ingredient_layout.addWidget(ingredient_line_edit)

        self.ingredients.append(ingredient_line_edit)

    def add_constraint_field(self):
        constraint_layout = QVBoxLayout()
        self.constraint_layout.addLayout(constraint_layout)

        constraint_label = QLabel('Constraint (name, value, type[min | max]):')
        constraint_layout.addWidget(constraint_label)

        constraint_line_edit = QLineEdit()
        constraint_layout.addWidget(constraint_line_edit)

        self.constraints[constraint_line_edit] = constraint_layout

    def solve_problem(self):
        # Read inputs
        cost = {}
        for ingredient_input in self.ingredients:
            values = ingredient_input.text().split(',')
            if len(values) == 2:
                try:
                    name = values[0]
                    cost[name] = float(values[1])
                except ValueError:
                    self.result_label.setText("Invalid input for one or more ingredients. Please enter numeric values.")
                    return

        constraints = []
        for constraint_input, constraint_layout in self.constraints.items():
            values = constraint_input.text().split(',')
            if len(values) == 3:
                try:
                    name = values[0]
                    value = float(values[1])
                    constraint_type = values[2].strip().lower()
                    if constraint_type not in ['min', 'max']:
                        raise ValueError
                    constraints.append((name, value, constraint_type))
                except ValueError:
                    self.result_label.setText("Invalid input for one or more constraints. Please enter numeric values.")
                    return

        # Initialize the model
        model = Model("Blending Problem")

        # Define decision variables
        amount = model.addVars(cost.keys(), name="amount")

        # Objective: Minimize total cost
        model.setObjective(sum(cost[i] * amount[i] for i in cost.keys()), GRB.MINIMIZE)

        # Constraints
        for name, value, constraint_type in constraints:
            if constraint_type == 'min':
                model.addConstr(sum(amount[i] for i in cost.keys()) >= value, name)
            elif constraint_type == 'max':
                model.addConstr(sum(amount[i] for i in cost.keys()) <= value, name)

        # Solve the model
        model.optimize()

        # Output results
        if model.status == GRB.OPTIMAL:
            result_text = "Optimal solution found:\n"
            for ingredient in cost.keys():
                result_text += f"{ingredient}: {amount[ingredient].x:.2f} units\n"
            self.result_label.setText(result_text)
        else:
            self.result_label.setText("No optimal solution found.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BlendingProblemGUI()
    ex.show()
    sys.exit(app.exec_())
