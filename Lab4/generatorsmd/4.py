def squares(a, b):
    for num in range(a, b + 1):  
        yield num ** 2  

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

for square in squares(a, b):
    print(square)
