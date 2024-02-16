"""
Q1. 
numbers = [1, 2, 3, 4, 5]
# TODO: Write a loop code that prints the difference between each number and its previous number.

# Write the loop code below.
"""

numbers = [1, 2, 3, 4, 5]
for i in range(1, len(numbers)):
    difference = numbers[i] - numbers[i-1]
    print(difference)
