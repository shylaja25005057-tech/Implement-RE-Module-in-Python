# Implement re module in Python

import re

text = "Python is easy. Python is powerful."

# Search for a word
result = re.search("Python", text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")

# Find all occurrences
result = re.findall("Python", text)
print("All matches:", result)

# Replace a word
result = re.sub("Python", "Java", text)
print("After replacement:", result)

# Split the string
result = re.split(" ", text)
print("Split words:", result)
