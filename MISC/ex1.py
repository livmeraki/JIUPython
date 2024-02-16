def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10

    return original_num == reversed_num

while(True):
    num = int(input("Enter a positive integer to check if it's a palindrome: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        break
    

if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")

def main():
    print("Hello World!")



if __name__ == "__main__":
    main()

print(__name__)
