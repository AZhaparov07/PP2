class MyClass:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input("Write a string: ")
    def printString(self):
        print(self.text.upper())

Mainstring = MyClass()
Mainstring.getString()
Mainstring.printString()
x = ("Apple","Home","Python")
print(type(x))