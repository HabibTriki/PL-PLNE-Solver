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
   git clone https://github.com/HabibTriki/PL-PLNE-Solver.git
   ```
2. **Navigate to the Directory**
   ```
   cd PL-PLNE-Solver
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

# Vehicle Routing Problem Solver

This repository contains a Python-based application that uses Gurobi and PyQt5 to solve the Vehicle Routing Problem (VRP). The application provides a graphical user interface for inputting the problem parameters and visualizing the solution.

## Features

- **Interactive Input**: Users can specify the number of vehicles, vehicle capacity, number of customers, and customer demands directly through the GUI.
- **Distance Matrix Configuration**: Users can input and edit the distance matrix directly within the application.
- **Optimization**: Leverages the power of the Gurobi optimizer to find solutions to the VRP.
- **Result Display**: Displays the optimization results directly through a message box within the GUI.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- PyQt5
- Gurobi Optimizer

Additionally, you need a valid Gurobi license to run the optimization. Gurobi offers academic licenses for free if you are associated with a recognized academic institution.

## Running the Application

To run the application, execute:
```
python VRPApp.py
```
This will launch the GUI, where you can input your data and solve the VRP.

## Usage

1. **Enter the Number of Vehicles** and their capacity.
2. **Specify the Number of Customers** and their demands.
3. **Input the Distance Matrix**: Fill out the matrix where each cell represents the distance from Node i to Node j.
4. **Solve the Problem**: Click the 'Solve VRP' button to compute the optimal routing.
5. **View Results**: The results will be displayed in a message box.

## Contributing

Contributions to this project are welcome. Feel free to fork the repo, add your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to Gurobi for providing the powerful optimization engine.
- Thanks to PyQt for the GUI framework.

![image](https://github.com/HabibTriki/PL-PLNE-Solver/assets/123327090/08316ed7-a5d7-43f6-b482-f063349aa469)
![image](https://github.com/HabibTriki/PL-PLNE-Solver/assets/123327090/ca151520-b2a4-4953-9dea-cda44e9b7966)
