def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# Test
print(factorial(5))  # Output: 120
 
