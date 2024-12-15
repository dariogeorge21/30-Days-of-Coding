a=int(input("Enter the total number of elemnts required"))
l=[]
for i in range(a):
	n=int(input("Enter"))
	l.append(n)
print(l)
print()
sum=0
b=len(l)
for i in range(b):
	sum=sum+l[i]
print(sum,"Is the sum of the list")
avg=sum/b
print(avg,"Is the average of the list") 
