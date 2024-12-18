def recursive_sum(numbers):
    if not numbers:
        return 0

    return numbers[0] + recursive_sum(numbers[1:])

# Example usage
numbers_list = [1, 2, 3, 4, 5]
result = recursive_sum(numbers_list)
print(f"Sum of the list: {result}")
