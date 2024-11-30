#Create a program to calculate the sum and #average of all elements in a list.

list1=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
sum=0	
for j in list1:
	sum+=j
print("The sum is",sum)

#Enter the limit:5
#Enter the number:25
#Enter the number:50
#Enter the number:75
#Enter the number:100
#Enter the number:150
#The sum is 400
