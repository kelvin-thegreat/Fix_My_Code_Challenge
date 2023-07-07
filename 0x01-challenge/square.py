#!/usr/bin/python3

class Square:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())

