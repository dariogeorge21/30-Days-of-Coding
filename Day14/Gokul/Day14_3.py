#Write a function named add_numbers() that takes two numbers as parameters and returns their sum
def add_numbers(a,b):
	sum=a+b
	return sum
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
result=add_numbers(num1,num2)
print(f"The sum is ",result)

#Enter the first number:3
#Enter the second number:5
#The sum is  8
