# create the class (blueprint) for rectangles
class Rectangle():

    # initialize attributes within class (constructor)
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # print out statement
    def __str__(self):
        return f"The area of the rectangle is {self.total_area()}."

    # find total area by multiplying length and width
    def total_area(self):
        return self.length * self.width

# create object
rect1 = Rectangle(5, 3)

# print out object
print(rect1)