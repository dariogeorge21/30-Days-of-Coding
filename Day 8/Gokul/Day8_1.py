#Write a Python program to find the largest #and smallest elements in a list.

list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
	list1.sort()
	
print("Largest number=",list1[-1])
print("smallest number=",list1[0])

#Enter the limit:5
#Enter the number:99
#Enter the number:1
#Enter the number:0
#Enter the number:-1
#Enter the number:1000
#Largest number= 1000
#smallest number= -1
