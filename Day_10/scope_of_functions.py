# Global & local Variables
# the variable created outside the function are called as global variable
# the variable created inside the function are called local variable

x=100   # global variable

def myfun():
    y=20
    print(y)

myfun() # this will come from loacl variable inside of the function
print(x) # this come form global variable

