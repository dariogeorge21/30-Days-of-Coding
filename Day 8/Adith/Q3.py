list1=[]
b=int(input("Enter the limit:"))
for num in range(b):
	num=int(input("Enter the number:"))
	list1.append(num)
 
print(list1)
a=list1[::-1]
print("reversed list:",a)
