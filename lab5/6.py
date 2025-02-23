import re

def replace_characters(text):
    pattern = r'[ ,.]'  
    return re.sub(pattern, ':', text)

sample_strings = ["Privet, mir. How is the weather?", "I love learning python", "This is a quiz. Let's solve it."]

for string in sample_strings:
    print(f"Original: '{string}'")
    print(f"Modified: '{replace_characters(string)}'\n")
