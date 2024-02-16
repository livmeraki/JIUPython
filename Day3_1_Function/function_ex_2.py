"""
Question #02
Create a function that converts Celsius to Fahrenheit. You don’t need to ask the number from the user, you can just state it as an argument. 
ex: result = celcius_fanrenheit(30)
HINT: The conversion formula is: F = C * 9/5 + 32.
"""

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Test the function
result = celsius_to_fahrenheit(30)
print(result)  # Output should be 86.0
