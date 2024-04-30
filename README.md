# Blending Problem Solver

This repository contains a Python application that solves the blending problem using the Gurobi optimization solver integrated with a PyQt5 GUI. The application allows users to input costs, protein, and fat values for three ingredients (Corn, Wheat, and Soy) and set constraints for minimum protein and maximum fat. The solver then computes the optimal amounts of each ingredient to meet the requirements at the lowest cost.

## Features

- **User Inputs**: Enter the cost, protein, and fat for each ingredient via a graphical user interface.
- **Optimization**: Utilizes Gurobi to solve the optimization problem based on the user inputs.
- **Dynamic Results**: Displays the optimal ingredient amounts directly in the GUI.

## Prerequisites

Before running this application, ensure you have the following installed:
- Python 3.x
- PyQt5
- Gurobi Optimizer

You also need a valid Gurobi license. For academic purposes, you can obtain a free academic license from the Gurobi website.

## Installation

Follow these steps to get the application running on your local machine:

1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/blending-problem-solver.git
   ```
2. **Navigate to the Directory**
   ```
   cd blending-problem-solver
   ```

3. **Install Required Packages**
   If you haven't already installed PyQt5 and Gurobi, you can install them using pip:
   ```
   pip install PyQt5
   pip install gurobipy
   ```

## Running the Application

To run the application, execute the following command in the root directory of the project:
```
python blending_problem_gui.py
```

## Usage

Upon launching the application, enter the cost, protein, and fat values for each of Corn, Wheat, and Soy in the format: `cost,protein,fat`. For example:
- `3.2,2,0.5` for Corn
- `2.5,1.5,0.8` for Wheat
- `4.0,3.5,0.3` for Soy

Then, set the minimum protein and maximum fat requirements and click the "Solve" button. The optimal amounts of each ingredient will be displayed below the button.

## Contributing

Contributions to this project are welcome. To contribute:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- Thanks to Gurobi for the optimization engine.
- Thanks to PyQt for the GUI framework.

### Notes:
- **License**: I assumed the MIT License for this template; you might want to choose a different license depending on your project's needs.
- 
# PLM problem :

![image](https://github.com/HabibTriki/PL-PLNE-Solver/assets/123327090/08316ed7-a5d7-43f6-b482-f063349aa469)
![image](https://github.com/HabibTriki/PL-PLNE-Solver/assets/123327090/ca151520-b2a4-4953-9dea-cda44e9b7966)
