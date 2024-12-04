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
if s1 in s2:
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")