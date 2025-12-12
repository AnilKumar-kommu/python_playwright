#a=10 # this value is the global scope

def display():
    a=20   # local scope of this  function
    print(a)
display()
#print(a) #NameError: name 'a' is not defined getting this error when calling the local scope variable in globallly
