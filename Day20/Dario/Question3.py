def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        # Add item to unique_list only if it's not already there
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Input: list with duplicates
input_list = [1, 2, 3, 4, 2, 3, 5, 1, 6, 7, 6]

# Remove duplicates
result = remove_duplicates(input_list)

# Output result
print("Original List:", input_list)
print("List after removing duplicates:", result)
