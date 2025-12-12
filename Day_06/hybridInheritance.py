# ==========================
# 🏢 Real-Time Example: Hybrid Inheritance
# Parent Class → Employee
# Child Classes → Developer, Tester
# Sub Child Class → TeamLead (inherits from both Developer and Tester)
# ==========================

# --------------------------
# Base Parent Class: Common details for all employees
# --------------------------
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


# --------------------------
# Child Class 1: Developer inherits from Employee
# --------------------------
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        # Initialize parent class
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def develop_code(self):
        print(f"{self.name} is writing code in {self.programming_language}")


# --------------------------
# Child Class 2: Tester inherits from Employee
# --------------------------
class Tester(Employee):
    def __init__(self, name, emp_id, salary, testing_tool):
        # Initialize parent class
        super().__init__(name, emp_id, salary)
        self.testing_tool = testing_tool

    def test_application(self):
        print(f"{self.name} is testing the application using {self.testing_tool}")


# --------------------------
# Sub Child Class: TeamLead inherits from BOTH Developer and Tester
# This creates Hybrid Inheritance (Multiple + Hierarchical)
# --------------------------
class TeamLead(Developer, Tester):
    def __init__(self, name, emp_id, salary, programming_language, testing_tool, team_size):
        # Call Developer's constructor (which also calls Employee using super())
        super().__init__(name, emp_id, salary, programming_language)
        self.testing_tool = testing_tool    # Inherit testing capability
        self.team_size = team_size          # Extra property for TeamLead

    def manage_team(self):
        print(f"{self.name} manages a team of {self.team_size} members")

    def show_full_role(self):
        print(f"{self.name} can develop in {self.programming_language}, test with {self.testing_tool}, and lead a team.")


# ==========================
# 🎯 Real-Time Execution Part
# ==========================

# Create Developer object
dev = Developer("Anil", "E201", 85000, "Python")

# Create Tester object
tester = Tester("Ravi", "E202", 75000, "Selenium")

# Create TeamLead object (inherits from Developer and Tester)
lead = TeamLead("Kiran", "E203", 95000, "Java", "Postman", 5)

# --------------------------
# Developer actions
# --------------------------
print("=== Developer Details ===")
dev.show_details()
dev.develop_code()

# --------------------------
# Tester actions
# --------------------------
print("\n=== Tester Details ===")
tester.show_details()
tester.test_application()

# --------------------------
# TeamLead actions (Hybrid behavior)
# --------------------------
print("\n=== TeamLead Details ===")
lead.show_details()       # from Employee
lead.develop_code()       # from Developer
lead.test_application()   # from Tester
lead.manage_team()        # specific to TeamLead
lead.show_full_role()     # specific to TeamLead
