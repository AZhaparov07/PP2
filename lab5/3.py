import re

def match_pattern(text):
    pattern = r'^[a-z]+_[a-z]+$'  
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

sample_strings = ["love_python", "testing_string", "Testing_String", "helloWorld", "world_hello"]

for string in sample_strings:
    print(f"'{string}': {match_pattern(string)}")
