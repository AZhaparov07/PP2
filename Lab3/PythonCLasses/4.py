import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates of point: {self.x} and {self.y}")
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        print(f"New coordinates of point: {self.x} and {self.y}")
    def dist(self, self2):
        #formula is d = sqrt(((x2 - x1)power of 2) + ((y2 - y1)power of 2))
        return math.sqrt((self.x - self2.x)**2 + (self.y - self2.y)**2)
x1 = int(input("First coordinate 1: "))
y1 = int(input("Second coordinate 1: "))
x2 = int(input("First coordinate 2: "))
y2 = int(input("Second coordinate 2: "))

Point1 = Point(x1,y1)
Point2 = Point(x2,y2)

Point1.show()
Point2.show()

print("Distance is ", Point1.dist(Point2))

x3 = int(input("New first coordinate for first point: "))
y3 = int(input("New second coordinate for first point: "))
x4 = int(input("New first coordinate for second point: "))
y4 = int(input("New second coordinate for second point: "))

Point1.move(x3,y3)
Point2.move(x4,y4)
Point1.show()
Point2.show()
