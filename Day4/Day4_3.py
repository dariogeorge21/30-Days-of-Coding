n=int(input("Enter the number:"))

reverse=0

while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)

#Enter the number:1243
#3421