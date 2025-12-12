# ==========================
# 🏢 Real-Time Example: Hierarchical Inheritance
# Parent Class → Employee
# Child Classes → Developer, Tester, Manager
# ==========================

# --------------------------
# Parent Class: Common features for all employees
# --------------------------
class Employee:
    # Constructor: initializes common employee details
    def __init__(self, name, emp_id, salary):
        self.name = name            # Employee name
        self.emp_id = emp_id        # Employee ID
        self.salary = salary        # Employee salary

    # Common method for all employees
    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


# --------------------------
# Child Class 1: Developer inherits from Employee
# --------------------------
class Developer(Employee):
    # Constructor for Developer
    def __init__(self, name, emp_id, salary, programming_language):
        # Call the parent (Employee) constructor using super()
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language  # Extra property specific to Developer

    # Developer-specific method
    def show_role(self):
        print(f"{self.name} works as a Developer using {self.programming_language}")


# --------------------------
# Child Class 2: Tester inherits from Employee
# --------------------------
class Tester(Employee):
    # Constructor for Tester
    def __init__(self, name, emp_id, salary, testing_tool):
        # Initialize parent properties
        super().__init__(name, emp_id, salary)
        self.testing_tool = testing_tool  # Extra property specific to Tester

    # Tester-specific method
    def show_role(self):
        print(f"{self.name} works as a Tester using {self.testing_tool}")


# --------------------------
# Child Class 3: Manager inherits from Employee
# --------------------------
class Manager(Employee):
    # Constructor for Manager
    def __init__(self, name, emp_id, salary, team_size):
        # Call the parent constructor
        super().__init__(name, emp_id, salary)
        self.team_size = team_size  # Extra property specific to Manager

    # Manager-specific method
    def show_role(self):
        print(f"{self.name} is a Manager handling a team of {self.team_size} people")


# ==========================
# 🎯 Real-Time Execution Part
# ==========================

# Create Developer object
dev = Developer("Anil", "E101", 80000, "Python")

# Create Tester object
tester = Tester("Ravi", "E102", 70000, "Selenium")

# Create Manager object
manager = Manager("Kiran", "E103", 95000, 10)

# --------------------------
# Call methods for Developer
# --------------------------
print("=== Developer Details ===")
dev.show_details()  # Inherited method from Employee
dev.show_role()     # Developer-specific method

# --------------------------
# Call methods for Tester
# --------------------------
print("\n=== Tester Details ===")
tester.show_details()  # Inherited method
tester.show_role()     # Tester-specific method

# --------------------------
# Call methods for Manager
# --------------------------
print("\n=== Manager Details ===")
manager.show_details()  # Inherited method
manager.show_role()     # Manager-specific method
