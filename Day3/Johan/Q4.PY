
l=[]
for i in range (3):
    n=int(input("Enter"))
    l.append(n)
l.sort()
print(l)
if l[0]+l[1]>l[2]:
    print("It is a Triangle")
else:
    print("Not a Triangle")