numbers = list(range(1,102))
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, numbers))
print(prime_numbers)