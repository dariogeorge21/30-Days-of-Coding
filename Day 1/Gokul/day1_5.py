#Question 5 : Write a program to find the square of the smallest numbers among 3 numbers as input from user?
list=[]
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

list.append(num1)
list.append(num2)
list.append(num3)

list.sort()

print(f"The smallest number is {list[0]}")
print(f"The square of {list[0]} is {list[0]*list[0]}")

#output
#Enter the first number:8
#Enter the second number:4
#Enter the third number:5
#The smallest number is 4
#The square of 4 is 16