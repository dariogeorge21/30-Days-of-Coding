l=[]
a=int(input("Eneter the amount of elements in the list: "))
for i in range(a):
    b=int(input("Enter the element: "))
    l.append(b)
print()
x=int(input("Enter the element to be searched: "))
y=l.count(x)
print("No of occurences: ",y)