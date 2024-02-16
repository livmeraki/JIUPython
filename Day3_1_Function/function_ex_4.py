"""
Question #04
Develop a function that checks if a given string is a palindrome (reads the same forwards and backward, ignoring spaces and cases). 

def is_palindrome(string):
    TODO: COMPLETE THIS FUNCTION

# Test the function
result = is_palindrome("Able was I, ere I saw Elba")
print(result)  # Output should be True
"""
def is_palindrome(string):
    processed_string = ' '.join(string.lower().split())
    return processed_string == processed_string[::-1]

# Test the function
result = is_palindrome("test case esac tset")
print(result)  # Output should be True

