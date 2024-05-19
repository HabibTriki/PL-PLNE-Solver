import sys
from gurobipy import Model, GRB
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QGroupBox

class BlendingProblemGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ingredients = []
        self.constraints = []
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Blending Problem Solver')

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        title_label = QLabel('Blending Problem')
        title_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        main_layout.addWidget(title_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_layout = QVBoxLayout(scroll_widget)

        ingredient_group_box = QGroupBox("Ingredients")
        scroll_layout.addWidget(ingredient_group_box)
        self.input_layout = QVBoxLayout()
        ingredient_group_box.setLayout(self.input_layout)
        self.add_ingredient_field()

        add_ingredient_btn = QPushButton('Add Ingredient')
        add_ingredient_btn.clicked.connect(self.add_ingredient_field)
        scroll_layout.addWidget(add_ingredient_btn)

        constraint_group_box = QGroupBox("Constraints")
        scroll_layout.addWidget(constraint_group_box)
        self.constraint_layout = QVBoxLayout()
        constraint_group_box.setLayout(self.constraint_layout)
        self.add_constraint_field()

        add_constraint_btn = QPushButton('Add Constraint')
        add_constraint_btn.clicked.connect(self.add_constraint_field)
        scroll_layout.addWidget(add_constraint_btn)

        submit_btn = QPushButton('Solve')
        submit_btn.clicked.connect(self.solve_problem)
        main_layout.addWidget(submit_btn)

        self.result_label = QLabel('')
        self.result_label.setWordWrap(True)
        main_layout.addWidget(self.result_label)

        back_btn = QPushButton('Back')
        back_btn.clicked.connect(self.close)
        main_layout.addWidget(back_btn)

    def add_ingredient_field(self):
        ingredient_layout = QHBoxLayout()

        ingredient_label = QLabel('Ingredient (name, cost, constraint1, value1, constraint2, value2, ...):')
        ingredient_layout.addWidget(ingredient_label)

        self.input_layout.addLayout(ingredient_layout)

        ingredient_line_edit = QLineEdit()
        self.input_layout.addWidget(ingredient_line_edit)

        self.ingredients.append(ingredient_line_edit)

    def add_constraint_field(self):
        constraint_layout = QHBoxLayout()

        constraint_label = QLabel('Constraint (constraint, value, type[min | max]):')
        constraint_layout.addWidget(constraint_label)

        self.constraint_layout.addLayout(constraint_layout)

        constraint_line_edit = QLineEdit()
        self.constraint_layout.addWidget(constraint_line_edit)

        self.constraints.append(constraint_line_edit)

    def solve_problem(self):
        cost = {}
        constraints = {}
        for ingredient_input in self.ingredients:
            values = ingredient_input.text().split(',')
            if len(values) >= 3 and len(values) % 2 == 1:
                try:
                    name = values[0].strip()
                    cost[name] = float(values[1])
                    constraints[name] = {values[i].strip(): float(values[i+1]) for i in range(2, len(values), 2)}
                except ValueError:
                    self.result_label.setText("Invalid input for one or more ingredients. Please enter numeric values.")
                    return

        constraints = []
        for constraint_input in self.constraints:
            values = constraint_input.text().split(',')
            if len(values) == 3:
                try:
                    constraint = values[0].strip()
                    value = float(values[1])
                    constraint_type = values[2].strip().lower()
                    if constraint_type not in ['min', 'max']:
                        raise ValueError
                    constraints.append((constraint, value, constraint_type))
                except ValueError:
                    self.result_label.setText("Invalid input for one or more constraints. Please enter numeric values.")
                    return

        model = Model("Blending Problem")

        amount = model.addVars(cost.keys(), name="amount")

        model.setObjective(sum(cost[i] * amount[i] for i in cost.keys()), GRB.MINIMIZE)

        for constraint, value, constraint_type in constraints:
            if constraint_type == 'min':
                model.addConstr(sum(constraints[i].get(constraint, 0) * amount[i] for i in cost.keys()) >= value, constraint + "_min")
            elif constraint_type == 'max':
                model.addConstr(sum(constraints[i].get(constraint, 0) * amount[i] for i in cost.keys()) <= value, constraint + "_max")

        model.optimize()

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
