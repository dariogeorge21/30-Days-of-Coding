def sum_of_elements(my_list):
    total = 0  # Initialize the sum to 0
    for num in my_list:
        total += num  # Add each element to the total
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
result = sum_of_elements(my_list)
print("The sum of all elements in the list is:", result)
