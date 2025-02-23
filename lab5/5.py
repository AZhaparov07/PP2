import re

def match_pattern(text):
    pattern = r'^a.*b$'  
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

sample_strings = ["ba", "bxb", "a123b", "acb", "b", "a", "cva", "a_c"]

for string in sample_strings:
    print(f"'{string}': {match_pattern(string)}")
