import re

def camel_to_snake(text):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()  

sample_strings = ["HelloWorld", "ConvertingToString"]

for string in sample_strings:
    print(f"Original: '{string}'")
    print(f"Snake case: '{camel_to_snake(string)}'\n")
