x=int(input("Enter the total number of elemnts required"))
l=[]
for i in range(x):
	n=int(input("Enter"))
	l.append(n)
print(l)
y=int(input("Enter the number which you need occurence"))
print(l.count(y))