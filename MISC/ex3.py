def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


n = int(input("Enter the number of Fibonacci terms to generate: "))
if n <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    fibonacci_sequence = generate_fibonacci(n)
    print(f"The Fibonacci sequence up to {n} terms is: {fibonacci_sequence}")

