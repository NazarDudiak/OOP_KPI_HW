class Rectangle:
    def __init__(self, length=0.0, width=0.0):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

    # getter method
    def get_attributes(self):
        return self.length, self.width

    # setter method
    def set_attributes(self, length, width):
        if (type(length) == float) and (type(width) == float):
            if ((length > 0.0) and (length < 20.0)) and ((width > 0.0) and (width < 20.0)):
                self.length = length
                self.width = width
            else:
                return "Error!"
        else:
            return "Error!"


rectangle_01 = Rectangle()

rectangle_01.set_attributes(4.5, 16.0)

print("Square:", rectangle_01.square())
print("Perimeter:", rectangle_01.perimeter())
