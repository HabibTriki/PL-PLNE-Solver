import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from gurobipy import Model, GRB

def resoudre_probleme(x_A_val, x_B_val):
    # Créer un nouveau modèle avec Gurobi
    mod = Model("maximisation_profit")

    # Définir les variables
    x_A = mod.addVar(vtype=GRB.INTEGER, name="x_A")
    x_B = mod.addVar(vtype=GRB.INTEGER, name="x_B")

    # Définir la fonction objectif
    mod.setObjective(1450 * x_A + 1800 * x_B, GRB.MAXIMIZE)

    # Ajouter les contraintes de temps de fabrication
    mod.addConstr(10 * x_A + 8 * x_B <= 300, "Preparation")
    mod.addConstr(6 * x_A + 4 * x_B <= 150, "Assemblage")
    mod.addConstr(9 * x_A + 7 * x_B <= 250, "Finition")

    # Ajouter les contraintes d'engagement minimum et de capacité du marché
    mod.addConstr(x_A >= x_A_val, "Engagement_A")
    mod.addConstr(x_B >= x_B_val, "Engagement_B")
    mod.addConstr(x_A <= 10, "Limite_A")
    mod.addConstr(x_B <= 10, "Limite_B")

    # Optimiser le modèle
    mod.optimize()

    # Vérifier si une solution optimale a été trouvée
    if mod.status == GRB.OPTIMAL:
        # Récupérer les valeurs des variables et le profit total
        solution_x_A = x_A.x
        solution_x_B = x_B.x
        profit_total = mod.objVal
    else:
        # Si aucune solution n'est trouvée, retourner des valeurs nulles ou appropriées
        solution_x_A = None
        solution_x_B = None
        profit_total = None

    return solution_x_A, solution_x_B, profit_total


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Disposition verticale
        layout = QVBoxLayout()

        # Ajouter des champs de texte pour l'input de l'utilisateur
        self.input_x_A = QLineEdit(self)
        self.input_x_B = QLineEdit(self)
        self.solve_button = QPushButton('Résoudre', self)
        self.solve_button.clicked.connect(self.on_click)

        # Ajouter des champs de texte à la disposition
        layout.addWidget(QLabel('Nombre de bibliothèques modèle A'))
        layout.addWidget(self.input_x_A)
        layout.addWidget(QLabel('Nombre de bibliothèques modèle B'))
        layout.addWidget(self.input_x_B)
        layout.addWidget(self.solve_button)

        # Définir la disposition sur la fenêtre
        self.setLayout(layout)
        self.setWindowTitle('Maximisation de Profit')
        self.show()

    def on_click(self):
        # Lorsque le bouton est cliqué, lire les valeurs
        x_A_val = int(self.input_x_A.text())
        x_B_val = int(self.input_x_B.text())

        # Appeler la fonction de résolution de problème
        x_A_sol, x_B_sol, profit = resoudre_probleme(x_A_val, x_B_val)

        # Afficher les résultats (cet exemple affiche simplement les résultats dans le terminal)
        print(f"Solution: x_A={x_A_sol}, x_B={x_B_sol}, Profit={profit}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
