l=[]
a=int(input("Eneter the amount of elements in the list: "))
for i in range(a):
    b=int(input("Enter the element: "))
    l.append(b)
c=[]
for i in range(len(l)-1,-1,-1):
    c.append(l[i])
print(c)