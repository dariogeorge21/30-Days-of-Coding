x=int(input("Enter the total number of elemnts required"))
l=[]
for i in range(x):
	n=int(input("Enter"))
	l.append(n)
print(l)
print()
print(min(l),"Is smallest")
print(max(l),"Is largest")