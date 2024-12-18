def fibonacci(n):
    """
    Recursive function to calculate the nth Fibonacci number.
    :param n: The position of the Fibonacci number (1-based index).
    :return: The nth Fibonacci number.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0  # Base case: First Fibonacci number is 0
    elif n == 2:
        return 1  # Base case: Second Fibonacci number is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Input: position of the Fibonacci number
n = int(input("Enter the position (n) to find the nth Fibonacci number: "))

# Calculate and display the result
try:
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
except ValueError as e:
    print(e)
