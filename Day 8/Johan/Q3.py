x=int(input("Enter the total number of elemnts required"))
l=[]
for i in range(x):
	n=int(input("Enter"))
	l.append(n)
print(l)
y=len(l)
l1=[]
for j in range (y-1,-1,-1):
	z=l[j]
	l1.append(z)
print(l1)
	