# # while loop use in python
#
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# # Output:
# # 0
# # 1
# # 2
# # 3
# # 4
#
# # Using else with while loop
# count = 0
# while count < 3:
#     print(count)
#     count += 1
# else:
#     print("Loop completed")
# Output:
# 0
# 1
# 2
# Loop completed

# Using break to exit a while loop
# count = 0
# while count < 5:
#     if count == 3:
#         break
#     print(count)
#     count += 1
# # Output:
# # 0
# # 1
# # 2
#
# # Using continue to skip an iteration in while loop
# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(count)
# Output:
# 1
# 2
# 4
# 5

# Infinite loop example (commented out to prevent execution)
# while True:
#     print("This will run forever unless stopped manually")
# Output:
# This will run forever unless stopped manually

# Using pass statement in while loop
# count = 0
# while count < 5:
#     if count == 2:
#         pass  # Placeholder for future code
#     print(count)
#     count += 1
# Output:
# 0
# 1
# 2
# 3
# 4

# Nested while loops
# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print(f"i: {i}, j: {j}")
#         j += 1
#     i += 1
# Output:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# i: 1, j: 1
# i: 2, j: 0
# i: 2, j: 1

# Using a while loop real time example
# user_input = ""
# while user_input.lower() != "exit":
#     user_input = input("Type 'exit' to quit: ")
#     print(f"You typed: {user_input}")
# Output:
# Type 'exit' to quit: hello
# You typed: hello
# Type 'exit' to quit: exit
# You typed: exit

# Counting down using while loop
# count = 5
# while count > 0:
#     print(count)
#     count -= 1
# print("Liftoff!")
# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


# Using while loop in real time automation script
# import time
# seconds = 10
# while seconds > 0:
#     print(f"Time left: {seconds} seconds")
#     time.sleep(1)
#     seconds -= 1
# print("Time's up!")
# Output:
# Time left: 10 seconds
# Time left: 9 seconds
# Time left: 8 seconds
# Time left: 7 seconds
# Time left: 6 seconds
# Time left: 5 seconds
# Time left: 4 seconds
# Time left: 3 seconds
# Time left: 2 seconds
# Time left: 1 seconds
# Time's up!

# Using while loop to validate user input
# age = 0
# while age <= 0:
#     age = int(input("Please enter your age (must be positive): "))
# print(f"Your age is: {age}")
# Output:
# Please enter your age (must be positive): -5
# Please enter your age (must be positive): 0
# Please enter your age (must be positive): 25
# Your age is: 25


# Using while loop to booking system
#





