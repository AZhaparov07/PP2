numbers = list(map(int, input().split(' ')))
def isprime(num):
    if num < 2:
        return False
    for i in range(2, len(num)):
        if num % i == 0:
            return False
    return True    

def filter_prime(numbers):
    return list(filter(isprime, numbers))

primenumbers = filter_prime(numbers)
print(primenumbers)
