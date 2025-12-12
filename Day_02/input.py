 #input from the user

# a= input('enter the value of a: ')
# b= input('enter the value of b: ')
# #swapping
# a, b = b, a
# #printing the swapped values
# print('After swapping:')
# print('a: ' + a)
# print('b: ' + b)

# #input from the user
# a= input('enter the value of a: ')
# b= input('enter the value of b: ')
# #swapping using arithmetic operations
# a= str(int(a) + int(b))  # Convert to int for addition, then back to str
# b= str(int(a) - int(b))  # Convert to int for subtraction, then back to str
# a= str(int(a) - int(b))  # Convert to int for subtraction, then back to str
# #printing the swapped values
# print('After swapping:')
# print('a: ' + a)
# print('b: ' + b)

#input from the user
# a= input('enter the value of a: ')
# b= input('enter the value of b: ')
# #swapping using XOR bitwise operation
# a= str(int(a) ^ int(b))  # Convert to int for XOR, then back to str
# b= str(int(a) ^ int(b))  # Convert to int for XOR, then back to str
# a= str(int(a) ^ int(b))  # Convert to int for XOR, then back to str
# #printing the swapped values
# print('After swapping:')
# print('a: ' + a)
# print('b: ' + b)
#
# # input from the user
# weight =input("Enter your Weight:")
# height =input("Enter your height:")
# w=float(weight)
# h=float(height)
# BMI=w/(h**2)
# print('your body BMI is', BMI)

# taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"
modulus = num1 % num2 if num2 != 0 else "Undefined (cannot modulus by zero)"
# displaying the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")


