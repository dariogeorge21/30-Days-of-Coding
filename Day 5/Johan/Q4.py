l=[]
x=int(input("Enter total number required :"))
for i in range(x):
	n=int(input("Enter :"))
	l.append(n)
print(l)
y=len(l)
for j in range(y):
	if l[j]%2==0:
		print(l[j],"is even")
	if l[j]%2!=0:
		print(l[j],"is odd")