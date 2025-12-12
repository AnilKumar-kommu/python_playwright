# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived class 1 (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)  # Call the constructor of Person
        self.emp_id = emp_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

# Derived class 2 (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, team_size):
        super().__init__(name, age, emp_id, salary)  # Call constructor of Employee
        self.team_size = team_size

    def display_manager_info(self):
        print(f"Manages a team of: {self.team_size} members")

# Creating object of Manager (multilevel inheritance)
manager1 = Manager("Alice", 35, "E123", 90000, 10)

# Accessing all info
manager1.display_person_info()      # from Person
manager1.display_employee_info()    # from Employee
manager1.display_manager_info()     # from Manager
