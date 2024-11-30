#Question 5 : Write a menu driven program by asking the user to perform which arithmetic operator has to be used, and perform it by inputing 2 numbers?

operator=input("Enter the operator:")
first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))

if operator=="+":
    print(f"{first} {operator} {second} = {first+second}")
elif operator=="-":
    print(f"{first} {operator} {second} = {first-second}")
    
elif operator=="*":
    print(f"{first} {operator} {second} = {first*second}")
    
elif operator=="/":
    print(f"{first} {operator} {second} = {first/second}")

else:
    print("Invalid operator")
    
#Enter the operator:*
#Enter the first number:2
#Enter the second number:3
#2 * 3 = 6