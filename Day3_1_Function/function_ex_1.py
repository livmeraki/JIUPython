"""
Question #01

Create a function that takes 2 values from the user’s input and then prints the sum, sub, and multiplication result of those 2 inputted values. 

Hint
Input:
Enter value of a = 7
Enter value of b = 5

Expected output 
Sum is = 12
Sub is = 2
Multiplication is = 35
"""

def result (a,b) :
add = a+b
sub = a-b
mul = a*b
print (f"Sum is (sum), Sub is (sub), & Multiply is (mul]")
a = int (input ("Enter value of a: "))
b= int (input ("Enter value of b: "))
result (a, b)
