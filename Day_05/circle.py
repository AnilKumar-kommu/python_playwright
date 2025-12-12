


class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        self.circumference = 2 * self.pi * radius
        self.area = self.radius * self.pi * radius
        self.perimeter = self.radius * 2 * self.pi * radius
circle1 = Circle(5)
print(circle1.radius)
print(circle1.circumference)
print(circle1.area)
print(circle1.perimeter)
circle2 = Circle(5)
print(circle2.radius)
print(circle2.circumference)
print(circle2.area)