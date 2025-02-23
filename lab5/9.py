import re

def insert_spaces(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)  

sample_strings = ["HelloWorld", "SpaceBetweenStrings", "JavaIsIntersting"]

for string in sample_strings:
    print(f"Original: '{string}'")
    print(f"Modified: '{insert_spaces(string)}'\n")