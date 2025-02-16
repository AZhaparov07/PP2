def divisibleby_3and4(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num  

n = int(input("Enter a number: "))

for number in divisibleby_3and4(n):
    print(number, end=" ")
