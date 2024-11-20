#Q5.WAP find the square of the smallest numbers input from user
l=[]
x=int(input("Enter the total number reqired "))
for i in range(x):
    n=int(input("Enter the number"))
    l.append(n)

y=min(l)
print(y**2)