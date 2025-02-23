import re

def split_at_uppercase(text):
    return re.findall(r'[A-Z][a-z]*', text)  

sample_strings = ["HelloWorld", "UppercasingYes", "ImLoveJava"]

for string in sample_strings:
    print(f"Original: '{string}'")
    print(f"Split: {split_at_uppercase(string)}\n")
