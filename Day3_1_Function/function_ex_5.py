"""
Question #05
Write a function that distinguishes prime numbers. You must return True if the given number is prime and False if not. A prime number is a positive integer that only divides into 1 and itself.
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

숫자 = 11
결과 = is_prime(숫자)
print(f"{숫자}는 소수인가요? {결과}")
