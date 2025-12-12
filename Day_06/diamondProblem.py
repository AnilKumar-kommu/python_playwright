# ==========================
# 🏢 Real-Time Example: Diamond Problem + MRO
# Classes: Employee → Developer & Tester → TeamLead
# ==========================

# --------------------------
# Base Parent Class
# --------------------------
class Employee:
    def task(self):
        print("General employee task")

# --------------------------
# Child Class 1: Developer inherits from Employee
# --------------------------
class Developer(Employee):
    def task(self):
        print("Developer writes code")

# --------------------------
# Child Class 2: Tester inherits from Employee
# --------------------------
class Tester(Employee):
    def task(self):
        print("Tester tests the code")

# --------------------------
# Sub Child Class: TeamLead inherits from BOTH Developer and Tester
# This creates the Diamond Problem
# --------------------------
class TeamLead(Developer, Tester):
    # Inherits task() method from both Developer and Tester
    pass

# ==========================
# 🎯 Real-Time Execution Part
# ==========================

# Create a TeamLead object
lead = TeamLead()

# Call task method
# Python decides which task() to execute using MRO
lead.task()

# --------------------------
# Check MRO to understand the order
# --------------------------
print("\nMethod Resolution Order (MRO) for TeamLead:")
print(TeamLead.mro())
