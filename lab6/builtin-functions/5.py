def is_true(list):
    return all(list)  

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(is_true(tuple1))  
print(is_true(tuple2))  
