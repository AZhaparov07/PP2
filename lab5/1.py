import re

def match_pattern(text):
    pattern = r'^ab*$'  
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

sample_strings = ["a", "ab", "aab", "abbb", "ba", "ac", "aabbb"]

for string in sample_strings:
    print(f"'{string}': {match_pattern(string)}")
