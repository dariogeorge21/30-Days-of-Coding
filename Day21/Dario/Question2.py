def is_armstrong(number):
    """
    Function to check if a number is an Armstrong number.
    :param number: The number to check.
    :return: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to count its digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == number

# Input: Get the number from the user
try:
    num = int(input("Enter a number to check if it is an Armstrong number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is NOT an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")
