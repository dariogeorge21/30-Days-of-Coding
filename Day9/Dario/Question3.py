s1=set()
a=int(input("Enter the no of elements to be added in the set1: "))
for i in range(a):
    b=int(input("Enter the value to be added to set1: "))
    s1.add(b)
s2=set()
a=int(input("Enter the no of elements to be added in the set2: "))
for i in range(a):
    b=int(input("Enter the value to be added to set2: "))
    s2.add(b)
b=set()
b=s1|s2
print("Union of the sets: ",b)
i=set()
i=s1&s2
print("Intersection of the sets: ",i)
d=set()
d=s1-s2
print("Difference of sets: ",d)