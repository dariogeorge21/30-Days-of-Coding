list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)

count1=int(input("Enter the element:"))
list2=list1.count(count1)
print(f"Occurences of {count1} is", list2)
