num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

smallest = min(num1, num2, num3)
square = smallest ** 2

print(f"The smallest number is {smallest}, and its square is {square}.")