## Question 3: Write a program to find the smallest of three numbers entered by the user.

small=[]

for i in range(3):
    n=int(input("Enter the number:"))
    small.append(n)
small.sort()
print(f"The smallest number is {small[0]}")

#Enter the number:10
#Enter the number:100
#Enter the number:-5
#The smallest number is -5