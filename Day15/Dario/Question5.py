def power(x, n):
    if n == 0:  # Base case
        return 1
    return x * power(x, n - 1)  # Recursive case

# Test
print(power(2, 3))  # Output: 8
 
