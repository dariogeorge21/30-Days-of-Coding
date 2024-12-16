list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
	list1.sort()
	
print("Largest number=",list1[-1])
print("smallest number=",list1[0])

