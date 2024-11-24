#Count Digits in a Number
#Write a program to count the number of digits in a number entered by the user.


n=int(input("Enter the number:"))
count=0

while n>0:
    count=count+1
    n=n//10

print("The no of digits is",count)

#Enter the number:1313245675
#The no of digits is 10