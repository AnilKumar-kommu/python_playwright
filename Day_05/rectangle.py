class Rectangle:
    pi = 3.14
    def __init__(self,width,height):
        self.width = width
        self.height = height
        #def area(self):
       ## return self.width * self.height
    def perimeter(self):
        return self.width * self.height
    def area(self):
        return self.width * self.height
    def circumference(self):
        return self.width * self.height
    def seperation(self):
        return self.width * self.height
rect1=Rectangle(2,2)
print(rect1.area())
rect2=Rectangle(3,3)
print(rect2.area())





