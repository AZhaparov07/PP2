def reversedword():
    word = input("Write a string: ")
    return " ".join(word.split()[::-1])
    
print(reversedword())
