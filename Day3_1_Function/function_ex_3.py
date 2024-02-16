"""
Question #03
Create a function that calculates the factorial of a given number(complete the code below)


def calculate_factorial(number):
#TODO: Calculate the factorial of the given number (ex: 5)
        return factorial

# Test the function
result = calculate_factorial(5) #Given number is 5
print(result)  # Output should be 120

"""

def calculate_factorial(number):
    factorial = 1
    if number < 0:
        return "Factorial is not defined for negative numbers"
    elif number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            factorial *= i
        return factorial

# Test the function
result = calculate_factorial(5)
print(result)  # Output should be 120
