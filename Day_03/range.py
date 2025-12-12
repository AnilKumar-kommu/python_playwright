# range uisage examples in Python

# # Example 1: Generating a sequence of numbers from 0 to 4
# for i in range(5):
#     print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# range function is gerating numbers starting from 0 up to (but not including) 5

# Example 2: Generating a sequence of numbers from 1 to 9 with a step of 2
# for i in range(1, 10, 2):
#     print(i)
# Output:
# 1
# 3
# 5
# 7
# 9
# range function is generating numbers starting from 1 up to (but not including) 10 with a step of 2

# Example 3: Generating a sequence of numbers from 10 to 1 in reverse order
# for i in range(10, 0, -1):
#     print(i)
# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# range function is generating numbers starting from 10 down to (but not including) 0

# Example 4: Using range to iterate over a list by index
# fruits = ["apple", "banana", "cherry"]
# for i in range(len(fruits)):
#     print(f"Index {i}: {fruits[i]}")
# # Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry
# range function is generating indices from 0 to the length of the list (but not including the length)

# Example 5: Creating a list of numbers using range
# numbers = list(range(5))
# print(numbers)
# Output:
# [0, 1, 2, 3, 4]
# range function is generating numbers from 0 to 4 and converting it into a list


# Example 6: Using range in a for loop
# for i in range(3, 8):
#     print(i)
# Output:
# 3
# 4
# 5
# 6
# 7
# range function is generating numbers starting from 3 up to (but not including) 8

# Example 7: Using range with negative step
# for i in range(5, 0, -1):
#     print(i)
# Output:
# 5
# 4
# 3
# 2
# 1
# range function is generating numbers starting from 5 down to (but not including) 0

# Example 8: Using range to create a list of even numbers
# even_numbers = list(range(0, 21, 2))
# print(even_numbers)
# # Output:
# # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# # range function is generating even numbers from 0 to 20 and converting it into a list
#
# # Example 9: Using range and for loop to create a list of odd numbers
# odd_numbers = []
# for i in range(1, 20, 2):
#     odd_numbers.append(i)
# print(odd_numbers)
# # Output:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# range function is generating odd numbers from 1 to 19 and appending them to a list

# Example 10: Using range in POM for generating test data
test_data = []
for i in range(1, 6):
    test_data.append(f"TestData_{i}")
print(test_data)
# Output:
# ['TestData_1', 'TestData_2', 'TestData_3', 'TestData_4', 'TestData_5']
# range function is generating numbers from 1 to 5 and using them to create test data strings





