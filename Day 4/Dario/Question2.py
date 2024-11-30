a=int(input("Enter a number: "))
sum=0
while a>0:
    b=a%10
    sum+=b
    a=a//10
print ("Sum of digits:",sum)