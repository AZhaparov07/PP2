import re

def snake_to_camel(text):
    components = text.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


sample_strings = ["Privet_mit", "converting_this_one_to_string"]

for string in sample_strings:
    print(f"Original: '{string}'")
    print(f"CamelCase: '{snake_to_camel(string)}'\n")
