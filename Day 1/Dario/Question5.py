num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

smallest = min(num1, num2, num3)
square = smallest ** 2

print("The smallest number is",smallest, "and its square is ",square)