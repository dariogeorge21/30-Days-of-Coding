l=[]
a=int(input("Eneter the amount of elements in the list: "))
for i in range(a):
    b=int(input("Enter the element: "))
    l.append(b)

x=int(input("Enter the element to be searched: "))
if x in l:
    print(True)
else:
    print(False)
    