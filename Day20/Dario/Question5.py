def second_largest(numbers):
    """
    Function to find the second largest number in a list.
    :param numbers: List of integers or floats.
    :return: The second largest number.
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    
    # Initialize the largest and second largest
    largest = second = float('-inf')

    for num in numbers:
        if num > largest:  # New largest number found
            second = largest
            largest = num
        elif num > second and num != largest:  # New second largest found
            second = num

    if second == float('-inf'):
        raise ValueError("No valid second largest number found (list may contain duplicates of the same number).")

    return second


# Input: List of numbers
try:
    numbers = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
    result = second_largest(numbers)
    print(f"The second largest number is: {result}")
except ValueError as e:
    print(e)
