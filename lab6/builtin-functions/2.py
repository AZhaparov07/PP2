def count_case(word):
    upp_count = sum(1 for char in word if char.isupper()) 
    low_count = sum(1 for char in word if char.islower())  
    return upp_count, low_count

word = "I Love Kbtu"
upper, lower = count_case(word)
print("Uc letters:", upper)
print("Lc letters:", lower)
