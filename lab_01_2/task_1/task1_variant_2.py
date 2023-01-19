class Rectangle:
    def __init__(self):
        self.length = 1
        self.width = 1

    def setter_length(self, length):
        if (length > 0) and (length < 20):
            self.length = length
            return True
        else:
            return False

    def getter_length(self):
        return self.length

    def setter_width(self, width):
        if (width > 0) and (width < 20):
            self.width = width
            return True
        else:
            return False

    def getter_width(self):
        return self.width

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

    def area(self):
        return self.length * self.width
