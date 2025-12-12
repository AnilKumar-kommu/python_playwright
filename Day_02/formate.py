#formate use in python
def formate():
    name = "Alice"
    age = 30
    height = 5.7

    # Using f-strings (Python 3.6+)
    f_string = f"My name is {name}, I am {age} years old and {height} feet tall."
    print("Using f-strings:", f_string)

    # Using str.format() method
    str_format = "My name is {0}, I am {1} years old and {2} feet tall.".format(name, age, height)
    print("Using str.format():", str_format)

    # Using % operator
    percent_format = "My name is %s, I am %d years old and %.1f feet tall." % (name, age, height)
    print("Using % operator:", percent_format)
formate()
# End of the code


