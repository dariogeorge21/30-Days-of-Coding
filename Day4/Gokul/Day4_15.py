#Check Palindrome Number
#Write a program to check if a number is a palindrome (i.e., reads the same backward as forward) using a while loop.

n=int(input("Enter the number:"))

reverse=0
n1=str(n)
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
r2=str(reverse)
if n1==r2:
    print(f"{n1} is palindrome")
else:
    print(f"{n1} is not palindrome")
    
#Enter the number:131
#131 is palindrome

#Enter the number:134
#134 is nt palindrome

