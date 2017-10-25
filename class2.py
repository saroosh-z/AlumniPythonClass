import math
class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        return print(f"x:{self.x} \ny:{self.y}")

    def distance(self):
        distance = math.sqrt(self.x**2 + self.y**2)
        print(distance)

    def __str__(self):
        return "object point. point.x is {self.x} and point.y is {self.y}"



##create an object of class Point
a = Point(4,6)
#word2 = Point(5,5)

#word2.print_point()

a.print_point()
a.distance()
print(f'{a}')

##a is a class point,
#I want another point a1 which is equal to a
import copy
a2 = copy.copy(a)
#a2 = a
print (a2 is a)
#a3 = a2


print(a2.x)
