x=int(input("Enter the total number of elemnts :"))
s=set()
for i in range(x):
	n=int(input("Enter"))
	s.add(n)
print(s)
n1=int(input("Value to be removed"))
s.remove(n1)
print(s)