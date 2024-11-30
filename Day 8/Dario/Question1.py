l=[]
a=int(input("Eneter the amount of elements in the list: "))
for i in range(a):
    b=int(input("Enter the element: "))
    l.append(b)
l.sort()

print("Smallest Value : ",l[0])
print("Largest Value: ",l[-1])