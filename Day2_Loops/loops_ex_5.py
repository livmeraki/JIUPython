"""
Q5.
text = "Hello, world!"
# TODO: Create a loop code that converts an even index of a given string to lowercase letters and converts an odd index to uppercase letters to output all of them

# Write the loop code below.
"""

text = "Hello, world!"
result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].lower()
    else:
        result += text[i].upper()

print(result)
