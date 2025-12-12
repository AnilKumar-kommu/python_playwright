# list used in python
# list methods in python
#list used in python give me real time examples also with hints and comments
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']
# Accessing elements
print(fruits[0])  # 'apple'
print(fruits[-1])  # 'cherry'
# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
# Adding elements
fruits.append("date")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']
fruits.insert(1, "avocado")
print(fruits)  # ['apple', 'avocado', 'blueberry', 'cherry', 'date']
# Removing elements
fruits.remove("cherry")
print(fruits)  # ['apple', 'avocado', 'blueberry', 'date']
popped_fruit = fruits.pop()
print(popped_fruit)  # 'date'
print(fruits)  # ['apple', 'avocado', 'blueberry']
# List length
print(len(fruits))  # 3
# Iterating through a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# avocado
# blueberry
# Checking membership
print("banana" in fruits)  # False
print("apple" in fruits)   # True
# Sorting a list
fruits.sort()
print(fruits)  # ['apple', 'avocado', 'blueberry']
fruits.sort(reverse=True)
print(fruits)  # ['blueberry', 'avocado', 'apple']
# Reversing a list
fruits.reverse()
print(fruits)  # ['apple', 'avocado', 'blueberry']
# Copying a list
fruits_copy = fruits.copy()
print(fruits_copy)  # ['apple', 'avocado', 'blueberry']
# Clearing a list
fruits.clear()
print(fruits)  # []
# Real-time example: Managing a to-do list
todo_list = []
# Adding tasks
todo_list.append("Buy groceries")
todo_list.append("Clean the house")
todo_list.append("Pay bills")
print(f"To-Do List: {todo_list}")  # ['Buy groceries', 'Clean the house', 'Pay bills']
# Completing a task
completed_task = todo_list.pop(0)
print(f"Completed Task: {completed_task}")  # 'Buy groceries'
print(f"Updated To-Do List: {todo_list}")  # ['Clean the house', 'Pay bills']
# Inserting a high-priority task
todo_list.insert(0, "Finish project report")
print(f"Updated To-Do List: {todo_list}")  # ['Finish project report', 'Clean the house', 'Pay bills']

# Sorting tasks alphabetically
todo_list.sort()
print(f"Sorted To-Do List: {todo_list}")  # ['Clean the house', 'Finish project report', 'Pay bills']
# Finding the number of tasks
print(f"Number of tasks: {len(todo_list)}")  # 3
# Real-time example: Shopping cart management
shopping_cart = []
# Adding items to the cart
shopping_cart.append("Laptop")
shopping_cart.append("Headphones")
shopping_cart.append("Mouse")
print(f"Shopping Cart: {shopping_cart}")  # ['Laptop', 'Headphones', 'Mouse']
# Removing an item from the cart
shopping_cart.remove("Headphones")
print(f"Updated Shopping Cart: {shopping_cart}")  # ['Laptop', 'Mouse']
# Checking if an item is in the cart
print("Laptop" in shopping_cart)  # True
print("Headphones" in shopping_cart)  # False
# Total items in the cart
print(f"Total items in cart: {len(shopping_cart)}")  # 2
# Clearing the cart after checkout
shopping_cart.clear()
print(f"Shopping Cart after checkout: {shopping_cart}")  # []
# Merging two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(f"Merged List: {merged_list}")  # [1, 2, 3, 4, 5, 6]
# Finding the index of an element
index_of_3 = merged_list.index(3)
print(f"Index of 3: {index_of_3}")  # 2
# Counting occurrences of an element
count_of_2 = merged_list.count(2)
print(f"Count of 2: {count_of_2}")  # 1
# Slicing a list
sliced_list = merged_list[1:4]
print(f"Sliced List: {sliced_list}")  # [2, 3, 4]
# Extending a list with another list
list1.extend([7, 8, 9])
print(f"Extended List1: {list1}")  # [1, 2, 3, 7, 8, 9]
# List comprehension example
squared_numbers = [x**2 for x in range(1, 6)]
print(f"Squared Numbers: {squared_numbers}")  # [1, 4, 9, 16, 25]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Element at (1,2): {matrix[1][2]}")  # 6
# Flattening a nested list
flattened = [num for row in matrix for num in row]
print(f"Flattened List: {flattened}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Real-time example: Student grades management
student_grades = {}
# Adding grades for students
student_grades["Alice"] = [85, 90, 78]
student_grades["Bob"] = [88, 76, 92]
print(f"Student Grades: {student_grades}")  # {'Alice': [85, 90, 78], 'Bob': [88, 76, 92]}
# Calculating average grade for a student
alice_avg = sum(student_grades["Alice"]) / len(student_grades["Alice"])
print(f"Alice's Average Grade: {alice_avg}")  # 84.33333333333333
# Adding a new grade for Bob
student_grades["Bob"].append(95)
print(f"Updated Student Grades: {student_grades}")  # {'Alice': [85, 90, 78], 'Bob': [88, 76, 92, 95]}
# Finding the highest grade among all students
all_grades = [grade for grades in student_grades.values() for grade in grades]
highest_grade = max(all_grades)
print(f"Highest Grade: {highest_grade}")  # 95
# Finding the student with the highest average grade
highest_avg_student = max(student_grades, key=lambda student: sum(student_grades[student]) / len(student_grades[student]))
print(f"Student with Highest Average Grade: {highest_avg_student}")  # Bob

# Real-time example: Inventory management
inventory = {"apple": 50, "banana": 30, "orange": 20}
# Adding stock
inventory["banana"] += 20
print(f"Updated Inventory: {inventory}")  # {'apple': 50, 'banana': 50, 'orange': 20}
# Removing stock
inventory["orange"] -= 5
print(f"Updated Inventory: {inventory}")  # {'apple': 50, 'banana': 50, 'orange': 15}
# Checking stock levels
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")
# Output:
# apple: 50
# banana: 50
# orange: 15
# Finding items low in stock
low_stock_items = [item for item, quantity in inventory.items() if quantity < 20]
print(f"Low Stock Items: {low_stock_items}")  # ['orange']
# Total inventory count
total_items = sum(inventory.values())
print(f"Total Items in Inventory: {total_items}")  # 115

# Merging inventories
new_inventory = {"apple": 20, "grape": 40}
for item, quantity in new_inventory.items():
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
print(f"Merged Inventory: {inventory}")  # {'apple': 70, 'banana': 50, 'orange': 15, 'grape': 40}
# Finding the item with the highest stock
highest_stock_item = max(inventory, key=inventory.get)
print(f"Item with Highest Stock: {highest_stock_item}")  # apple
# Finding the item with the lowest stock
lowest_stock_item = min(inventory, key=inventory.get)
print(f"Item with Lowest Stock: {lowest_stock_item}")  # orange
# Sorting inventory by item name
sorted_inventory_by_name = dict(sorted(inventory.items()))
print(f"Inventory Sorted by Name: {sorted_inventory_by_name}")  # {'apple': 70, 'banana': 50, 'grape': 40, 'orange': 15}
# Sorting inventory by quantity
sorted_inventory_by_quantity = dict(sorted(inventory.items(), key=lambda item: item[1]))
print(f"Inventory Sorted by Quantity: {sorted_inventory_by_quantity}")  # {'orange': 15, 'grape': 40, 'banana': 50, 'apple': 70}

# Real-time example: Playlist management
playlist = []
# Adding songs to the playlist
playlist.append("Song A")
playlist.append("Song B")
playlist.append("Song C")
print(f"Playlist: {playlist}")  # ['Song A', 'Song B', 'Song C']
# Removing a song from the playlist
playlist.remove("Song B")
print(f"Updated Playlist: {playlist}")  # ['Song A', 'Song C']
# Checking if a song is in the playlist
print("Song A" in playlist)  # True
print("Song B" in playlist)  # False
# Total songs in the playlist
print(f"Total Songs in Playlist: {len(playlist)}")  # 2
# Clearing the playlist
playlist.clear()
print(f"Playlist after clearing: {playlist}")  # []
# Merging two playlists
playlist1 = ["Song A", "Song B"]
playlist2 = ["Song C", "Song D"]
merged_playlist = playlist1 + playlist2
print(f"Merged Playlist: {merged_playlist}")  # ['Song A', 'Song B', 'Song C', 'Song D']
# Finding the index of a song
index_of_song_c = merged_playlist.index("Song C")
print(f"Index of Song C: {index_of_song_c}")  # 2
# Counting occurrences of a song
count_of_song_a = merged_playlist.count("Song A")
print(f"Count of Song A: {count_of_song_a}")  # 1
# Slicing the playlist
sliced_playlist = merged_playlist[1:3]
print(f"Sliced Playlist: {sliced_playlist}")  # ['Song B', 'Song C']
# Extending a playlist with another playlist
playlist1.extend(["Song E", "Song F"])
print(f"Extended Playlist1: {playlist1}")  # ['Song A', 'Song B', 'Song E', 'Song F']
# List comprehension example: Creating a playlist of songs with 'A' in the title
