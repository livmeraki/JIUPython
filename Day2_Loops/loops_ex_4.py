"""
Q4.
word = input("Enter a word: ")
# TODO: Write a loop code to calculate and print the number of vowels in the entered word.

# Write the loop code below.
"""

word = input("Enter a word: ")
vowels = 'AEIOUaeiou'

total_vowel_count = 0

for char in word:
    if char in vowels:
        total_vowel_count += 1

print("Total number of vowels:", total_vowel_count)
