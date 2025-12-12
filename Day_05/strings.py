# strings use in python

greeting = "Hello, World!"
print(greeting)
print(greeting[0])  # Accessing first character
print(greeting[-1]) # Accessing last character

# Slicing
print(greeting[0:5])  # 'Hello'
print(greeting[7:])   # 'World!'
print(greeting[:5])   # 'Hello'

# String methods
print(greeting.lower())      # 'hello, world!'
print(greeting.upper())      # 'HELLO, WORLD!'
print(greeting.replace("World", "Python"))  # 'Hello, Python!'
print(greeting.split(", "))  # ['Hello', 'World!']

# String formatting
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Using f-string
print("My name is {} and I am {} years old.".format(name, age))  # Using format method
print("My name is %s and I am %d years old." % (name, age))  # Using % operator

# Multiline strings
multiline = """This is a multiline
string that spans multiple lines."""
print(multiline)

#rquote strings
raw_string = r"C:\Users\Alice\Documents"
print(raw_string)  # 'C:\Users\Alice\Documents'



# Escape characters
print("He said, \"Hello!\"")  # Using escape character for double quote
print('It\'s a beautiful day!') # Using escape character for single quote
print("Line1\nLine2")         # New line
print("Tab\tSeparated")       # Tab space

# String concatenation
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # 'Hello World'

# String length
print(len(greeting))  # 13

# Checking substring
print("World" in greeting)  # True
print("Python" not in greeting)  # True

# Iterating through a string
for char in greeting:
    print(char)
# Output:
# H
# e
# l
# l
# o
# ,
#
# W
# o
# r
# l
# d
# !

# Stripping whitespace
whitespace_str = "   Hello, World!   "
print(whitespace_str.strip())  # 'Hello, World!'
print(whitespace_str.lstrip()) # 'Hello, World!   '
print(whitespace_str.rstrip()) # '   Hello, World!'

# Finding substrings
print(greeting.find("World"))  # 7
print(greeting.index("Hello"))  # 0
print(greeting.count("l"))      # 3

# Joining strings
words = ["Hello", "from", "Python"]
print(" ".join(words))  # 'Hello from Python'
print("-".join(words))  # 'Hello-from-Python'
# Output:
# Hello, World!
# H
# !
# Hello
# World!
# Hello, Python

# strings use in python real time examples
user_input = "   python programming   "
cleaned_input = user_input.strip().lower()
print(f"Cleaned Input: '{cleaned_input}'")  # 'python programming'
keywords = cleaned_input.split()
print(f"Keywords: {keywords}")  # ['python', 'programming']
formatted_string = f"User is interested in {keywords[0]} and {keywords[1]}."
print(formatted_string)  # 'User is interested in python and programming.'
email_template = "Dear {name},\n\nThank you for joining {platform}.\n\nBest regards,\n{platform} Team"
personalized_email = email_template.format(name="Alice", platform="CodeLearn")
print(personalized_email)
# Output:
# Cleaned Input: 'python programming'
# Keywords: ['python', 'programming']
# User is interested in python and programming.
# Dear Alice,
#
# Thank you for joining CodeLearn.
#
# Best regards,
# CodeLearn Team

# Real time example: Log parsing
log_entry = '2024-06-01 12:00:00, INFO, User "alice" logged in from IP'
date, log_level, message = log_entry.split(", ", 2)
print(f"Date: {date}")          # '2024-06-01 12:00:00'
print(f"Log Level: {log_level}") # 'INFO'
print(f"Message: {message}")     # 'User "alice" logged in from IP'
username_start = message.find('"') + 1
username_end = message.find('"', username_start)
username = message[username_start:username_end]
print(f"Username: {username}")   # 'alice'
# Output:
# Date: 2024-06-01 12:00:00
# Log Level: INFO
# Message: User "alice" logged in from IP
# Username: alice