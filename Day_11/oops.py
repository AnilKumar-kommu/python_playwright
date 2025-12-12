

#Example 6: Class with constractor
# Syntax :   __int__():  --> constractor
#Constractor is used for Initialize the data
# it will invoke automatically when object is created


class Myclass:

    def __init__(self):   # it used for data initialization and print somthing
        print("this constractor..")
    def m1(self):
        print("hello")
    def m2(self,x,y):
        return x + y

mc=Myclass()
mc.m1()
print(mc.m2(10,20))

