"""
Q3.
names = ["Alice", "Bob", "Charlie", "David"]
# TODO: Write a loop code to calculate the length of each name in the given list. For each name, if the length is odd, add the length; if even, add  the length. Finally, print the total.

# Write the loop code below.

"""

names = ["Alice", "Bob", "Charlie", "David"]

# Loop code below.
odd_sum = 0
even_sum = 0

for name in names:
    if len(name) % 2 != 0:
        odd_sum += len(name)
    else:
        even_sum += len(name)

print("Sum of lengths with odd characters:", odd_sum)
print("Sum of lengths with even characters:", even_sum)


