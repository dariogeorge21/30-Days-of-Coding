def fibonacci(n):
    if n == 0:  # Base case
        return 0
    if n == 1:  # Base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Test
print(fibonacci(6))  # Output: 8
 
