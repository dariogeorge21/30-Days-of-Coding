def sum_of_digits(num):
    if num == 0:  # Base case
        return 0
    return num % 10 + sum_of_digits(num // 10)  # Recursive case

# Test
print(sum_of_digits(123))  # Output: 6
