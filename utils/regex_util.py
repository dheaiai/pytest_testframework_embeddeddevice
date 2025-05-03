import re

def extract_pattern(text: str, pattern: str):
    return re.findall(pattern, text)


def extract_error_codes():
    return None