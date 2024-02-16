def calc_factorial(num):
    factorial_result = 1
    for i in range(1, num + 1):
        factorial_result *= i
    return factorial_result

while(True):
    num = int(input("Enter a non-negative integer to calculate its factorial: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        break

result = calc_factorial(num)
print("The factorial of", num, "is:", result)
