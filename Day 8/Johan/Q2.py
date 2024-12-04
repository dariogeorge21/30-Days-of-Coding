=int(input("Enter the total number of elemnts required"))
l=[]
for i in range(x):
	n=int(input("Enter"))
	l.append(n)
print(l)
print()
sum=0
y=len(l)
for i in range(y):
	sum=sum+l[i]
print(sum,"Is the sum of the list")
avg=sum/y
print(avg,"Is the average of the list") 
