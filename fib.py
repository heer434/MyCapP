def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

n = int(input("Enter the number of Fibonacci terms you want to generate: "))
fibonacci_terms = generate_fibonacci(n)

print("Fibonacci Sequence:")
for term in fibonacci_terms:
    print(term, end=" ")
