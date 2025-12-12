#for and loop condtions use in python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
# Using range() to loop through a sequence of numbers
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# Looping with a step value
for i in range(0, 10, 2):
    print(i)
# Output:
# 0
# 2
# 4
# 6
# 8
# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Output:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# i: 1, j: 1
# i: 2, j: 0
# i: 2, j: 1
# Using else with for loop
for i in range(3):
    print(i)
else:
    print("Loop completed")
# Output:
# 0
# 1
# 2
# Loop completed

# Using break to exit a loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# Using continue to skip an iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4
# Looping through a list with index
fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    print(f"Index: {index}, Fruit: {fruits[index]}")
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# Looping through a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")
# Output:
# name: Alice
# age: 25
# city: New York
# Looping through a set
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
# Output (order may vary):
# red
# green
# blue

# Looping through a tuple
dimensions = (10, 20, 30)
for dimension in dimensions:
    print(dimension)
# Output:
# 10
# 20
# 30

# Using enumerate() to get index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# Using zip() to loop through multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# List comprehension with for loop
squares = [x**2 for x in range(5)]
print(squares)
# Output:
# [0, 1, 4, 9, 16]

# Dictionary comprehension with for loop
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)
# Output:
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension with for loop
squared_set = {x**2 for x in range(5)}
print(squared_set)
# Output:
# {0, 1, 4, 9, 16}

# real time project loos condition
# Example: Processing a list of orders and calculating total price
orders = [{"item": "apple", "price": 1.2, "quantity": 5},
            {"item": "banana", "price": 0.8, "quantity": 10},
            {"item": "cherry", "price": 2.5, "quantity": 3}]
total_price = 0
for order in orders:
    item_total = order["price"] * order["quantity"]
    total_price += item_total
    print(f"Processed order for {order['quantity']} {order['item']}(s): ${item_total:.2f}")
print(f"Total price for all orders: ${total_price:.2f}")
# Output:
# Processed order for 5 apple(s): $6.00
# Processed order for 10 banana(s): $8.00
# Processed order for 3 cherry(s): $7.50
# Total price for all orders: $21.50

# Example: Filtering a list of products based on stock availability
products = [{"name": "Laptop", "in_stock": True},
            {"name": "Smartphone", "in_stock": False},
            {"name": "Tablet", "in_stock": True},
            {"name": "Headphones", "in_stock": False}]
available_products = []
for product in products:
    if product["in_stock"]:
        available_products.append(product["name"])
print("Available products:", available_products)
# Output:
# Available products: ['Laptop', 'Tablet']
# Example: Generating a report of student grades
students = [{"name": "Alice", "grade": 85},
            {"name": "Bob", "grade": 92},
            {"name": "Charlie", "grade": 78},
            {"name": "David", "grade": 90}]
for student in students:
    status = "Passed" if student["grade"] >= 80 else "Failed"
    print(f"{student['name']} - Grade: {student['grade']} - {status}")
# Output:
# Alice - Grade: 85 - Passed
# Bob - Grade: 92 - Passed
# Charlie - Grade: 78 - Failed
# David - Grade: 90 - Passed

# Example: Sending notifications to users
users = [{"username": "user1", "email": "user1@example.com"," active": True},
            {"username": "user2", "email":"user2@example.com" , "active": False},
                {"username": "user3", "email": "user3@example.com", "active": True}]
for user in users:
    if user["active"]:
        print(f"Sending notification to {user['username']} at {user['email']}")
# Output:
# Sending notification to user1 at
# Sending notification to user3 at

# Example: Calculating the factorial of a number
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")
# Output:
# The factorial of 5 is 120

# Example: Creating a multiplication table
num = 3
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
# Output:
# Multiplication table for 3:
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

# Example: Finding prime numbers in a given range
start = 10
end = 30
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        print(num)
# Output:
# Prime numbers between 10 and 30:
# 11
# 13
# 17
# 19
# 23
# 29

# Example: Summing even numbers in a list