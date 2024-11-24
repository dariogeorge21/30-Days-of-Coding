

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3


square = smallest ** 2


print(f"The smallest number is: {smallest}")
print(f"The square of the smallest number is: {square}")


              𝗢𝗨𝗧𝗣𝗨𝗧


Enter the first number: 25
Enter the second number: 16
Enter the third number: 8
The smallest number is: 8.0
The square of the smallest number is: 64.0

[Program finished]