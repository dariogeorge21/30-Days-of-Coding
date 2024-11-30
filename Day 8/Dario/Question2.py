l=[]
a=int(input("Eneter the amount of elements in the list: "))
for i in range(a):
    b=int(input("Enter the element: "))
    l.append(b)
    sum=0
    for i in l:
        sum+=i
avg=0
print("Sum of element: ",sum)
avg=sum/a
print("Average is ",avg)