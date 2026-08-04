# Parent Class
class Shape:
    def area(self):
        print("Area of Shape")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle:", self.length * self.breadth)


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle:", 3.14 * self.radius * self.radius)


# Main Program
r = Rectangle(10, 5)
c = Circle(7)

r.area()
c.area()