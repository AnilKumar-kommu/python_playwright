

# --------------------------
# Parent Class
# --------------------------


class Employee:
    def task(self):
        print("General employee task")

# --------------------------
# Child Class 1
# --------------------------
class Developer(Employee):
    def task(self):
        print("Developer writes code")

# --------------------------
# Child Class 2
# --------------------------
class Tester(Employee):
    def task(self):
        print("Tester tests the code")

# --------------------------
# Child Class 3 (Diamond problem)
# --------------------------
class TeamLead(Developer, Tester):
    pass

# ==========================
# Execution
# ==========================
lead = TeamLead()
lead.task()  # Which task will be executed?
print(TeamLead.mro())