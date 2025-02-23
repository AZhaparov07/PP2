import re

def match_pattern(text):
    return bool(re.fullmatch(r'ab{2,3}', text))  

samples = ["a", "ab", "aab", "abbb", "abbb", "ba", "ac", "aaabb"]

for s in samples:
    print(f"'{s}': {match_pattern(s)}")
