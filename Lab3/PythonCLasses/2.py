class Shape:
    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def Area(self):
        return self.length ** 2

shape1 = Shape()
print(Shape.Area())

square1 = Square(3)
print(Square.Area())

