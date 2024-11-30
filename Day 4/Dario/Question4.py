a=int(input("Enter a number: "))
digit=0
while a>0:
    digit+=1
    a=a//10
print ("Length of number:",digit)