def ispalindrome():
    word = input()
    if(word == word[::-1]):
        return "Palindrome"
    else:
        return "Not palindrome"
print(ispalindrome())