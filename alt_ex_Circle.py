from math import pi

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        area = pi * self.radius * self.radius
        return area

circle = Circle(6)
print(circle.area())