# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        # Display basic person info
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived class 1 (Student) - inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id, course):
        Person.__init__(self, name, age)  # Explicitly call Person constructor
        self.student_id = student_id
        self.course = course

    def display_student_info(self):
        # Display student-specific info
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

# Derived class 2 (Teacher) - inherits from Person
class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        Person.__init__(self, name, age)  # Explicitly call Person constructor
        self.teacher_id = teacher_id
        self.subject = subject

    def display_teacher_info(self):
        # Display teacher-specific info
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Subject: {self.subject}")

# Hybrid class: TeachingAssistant (Student + Teacher)
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, course, teacher_id, subject, ta_hours):
        # Initialize Student part
        Student.__init__(self, name, age, student_id, course)
        # Initialize Teacher part
        Teacher.__init__(self, name, age, teacher_id, subject)
        # Initialize TeachingAssistant-specific attribute
        self.ta_hours = ta_hours

    def display_ta_info(self):
        # Display Teaching Assistant info
        print(f"TA Hours per week: {self.ta_hours}")

# Create TeachingAssistant object
ta1 = TeachingAssistant("Bob", 22, "S101", "Computer Science", "T201", "Python Programming", 15)

# Accessing info from all parent classes
ta1.display_person_info()      # from Person
ta1.display_student_info()     # from Student
ta1.display_teacher_info()     # from Teacher
ta1.display_ta_info()          # from TeachingAssistant
