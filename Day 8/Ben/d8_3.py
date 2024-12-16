list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
 
print(list1)
rev=list1[::-1]
print("reversed list:",rev)
