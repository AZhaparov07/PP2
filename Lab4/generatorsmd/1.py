def generator_of_square(Number):
    for i in range(Number + 1):  
        yield i ** 2  

Number = int(input("Enter a number: "))
for square in generator_of_square(Number):
    print(square)
