def reverse_tuple(input_tuple):
    """
    Function to reverse a tuple.
    :param input_tuple: The input tuple.
    :return: A new tuple with elements in reverse order.
    """
    return input_tuple[::-1]  # Slicing to reverse the tuple

# Input: Tuple from the user
input_tuple = tuple(input("Enter elements of the tuple separated by spaces: ").split())

# Reverse the tuple
reversed_tuple = reverse_tuple(input_tuple)

# Display the result
print("Original Tuple:", input_tuple)
print("Reversed Tuple:", reversed_tuple)
