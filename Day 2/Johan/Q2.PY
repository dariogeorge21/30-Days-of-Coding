#Q2.WAP to check weather the number X is a multiple of Y or not?
x=int(input("Enter the value"))
y=int(input("Enter the value"))
if x%y==0:
    print(x,"is a multiple of ",y)
else:
    print(x,"is not a multiple of ",y)