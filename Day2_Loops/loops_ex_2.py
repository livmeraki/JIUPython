"""
Q2. 
sentence = "The quick brown fox jumps over the lazy dog"
# TODO: Write a loop code that prints the result of capitalizing the first letter of each word.

# Write the loop code below.
"""

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
for word in words:
    capitalized_word = word[0].upper() + word[1:]
    print(capitalized_word, end=" ")

