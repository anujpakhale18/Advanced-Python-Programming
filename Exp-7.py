# Experiment 7
# Title: Regular Expressions (Regex) - Pattern matching.

import re

def find_emails(text):
    pattern = r'\w+@\w+\.\w+'
    return re.findall(pattern, text)

text = input("Enter text: ")

emails = find_emails(text)

print("Email addresses:", emails)