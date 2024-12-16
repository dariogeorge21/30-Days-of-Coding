list1=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
sum=0	
for j in list1:
	sum+=j
print("The sum is",sum)
