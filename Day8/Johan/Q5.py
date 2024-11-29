x=int(input("Enter the total number of elemnts required"))
l=[]
for i in range(x):
	n=int(input("Enter"))
	l.append(n)
print(l)
y=int(input('Enter the number to check :'))
if y in l:
	print("True")
else:
	print("False")