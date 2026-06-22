# Classes are used to define new types, used to model real concepts e.g., shopping cart

# Classes we already know:
# Ints
# String
# Boolean
# Lists
# Dictionary


class Point: #Pascal naming convention for classes (capitalise every word, CamelCase), vars and funcs are in lowercase and use underscores
    def move(self):
        print("move")
    def draw(self):
        print("draw")


# An object is an instance of a class

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point() # different object from the first one
# print(point2.x) --- will come up with this error --> AttributeError: 'Point' object has no attribute 'x'

# Each object is a different instance of our Point class

point2.x = 1

