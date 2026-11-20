# Implement-RE-Module-in-Python

Aim:
To implement the re module in Python.

Algorithm:
1.Start.

2.Import the re module.

3.Create a string.

4.Use search() to search for a pattern.

5.Use findall() to find all matching patterns.

6.Use sub() to replace a pattern.

7.Display the result.

8.Stop.

Source Code:
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
<img width="1152" height="332" alt="image" src="https://github.com/user-attachments/assets/8828c002-c183-4140-9faa-452b355e4ab0" />
