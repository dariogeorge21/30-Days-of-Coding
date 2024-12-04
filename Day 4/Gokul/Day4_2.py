#Sum of Digits
#Write a program to find the sum of the digits of a number entered by the user using a while loop.

n=int(input("Enter the number:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
    
print(f"The sum of the digits is {sum}")
  
# Enter the number:145
#The sum of the digits is 10 