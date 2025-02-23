import re

def match_pattern(text):
    pattern = r'^[A-Z][a-z]+$' 
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

sample_strings = ["Prviet", "proverka", "PROVERKA", "testing", "PrivetWorld", "Java", "python"]

for string in sample_strings:
    print(f"'{string}': {match_pattern(string)}")
