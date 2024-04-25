from gurobipy import Model, GRB, quicksum

def get_input(prompt, cast_type=int, is_list=False):
    while True:
        try:
            value = input(prompt)
            if is_list:
                return [cast_type(item) for item in value.split()]
            return cast_type(value)
        except ValueError:
            print(f"Invalid input, please enter again using correct type {cast_type.__name__}")

def main():
    # User input for problem parameters
    N = get_input("Enter the number of locations (including depot): ")  # Total locations
    V = get_input("Enter the number of vehicles: ")
    W = get_input("Enter the maximum capacity for each vehicle: ")
    T = get_input("Enter the maximum distance each vehicle can travel: ")
    L = get_input("Enter the maximum number of customers each vehicle can service: ")

    print("Enter the demands at each location (starting with depot, which should be 0):")
    Q = get_input("", cast_type=int, is_list=True)

    if len(Q) != N:
        print("The number of demand inputs does not match the number of locations. Exiting.")
        return

    print("Enter the distance matrix (rows one by one, separated by space):")
    C = []
    for i in range(N):
        row = get_input(f"Row {i+1}: ", cast_type=int, is_list=True)
        if len(row) != N:
            print("The number of distances does not match the number of locations. Exiting.")
            return
        C.append(row)

    # Create a new model
    m = Model("CVRP")

    # Decision variables
    x = m.addVars(N, N, vtype=GRB.BINARY, name="x")
    u = m.addVars(N, vtype=GRB.CONTINUOUS, name="u")  # for subtour elimination

    # Objective: Minimize the total distance traveled
    m.setObjective(quicksum(C[i][j] * x[i, j] for i in range(N) for j in range(N) if i != j), GRB.MINIMIZE)

    # Constraints
    # Each customer is visited exactly once
    for j in range(1, N):
        m.addConstr(quicksum(x[i, j] for i in range(N) if i != j) == 1)

    # Each vehicle leaves the depot
    m.addConstr(quicksum(x[0, j] for j in range(1, N)) == V)

    # Each vehicle returns to the depot
    m.addConstr(quicksum(x[i, 0] for i in range(1, N)) == V)

    # Capacity constraints
    for i in range(1, N):
        m.addConstr(quicksum(x[i, j] * Q[j] for j in range(N) if i != j) <= W)

    # Subtour elimination and other constraints
    for i in range(1, N):
        for j in range(1, N):
            if i != j:
                m.addConstr(u[i] - u[j] + L * x[i, j] <= L - 1)

    # Solve the model
    m.optimize()

    # Print solution
    if m.status == GRB.OPTIMAL:
        solution = m.getAttr('x', x)
        for i in range(N):
            for j in range(N):
                if solution[i, j] > 0.5:
                    print(f"Vehicle travels from {i} to {j}")

if __name__ == "__main__":
    main()
