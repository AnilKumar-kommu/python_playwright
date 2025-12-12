#1. arbitrary or variables - length arguments
#2. Positional or Required Arguments
#3. Keyword Arguments

#example 1: Function with Arbitrary Arguments

# def sum_function(a,b):
#     return a+b
# print(sum_function(5,6))

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
res=largest(10,20)
print(res)
print(type(res))

