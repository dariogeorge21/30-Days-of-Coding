#Write a Python program to reverse a given list without using the built-in reverse() method.
list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
 
print(list1)
rev=list1[::-1]
print("reversed list:",rev)

#Enter the limit:4
#Enter the number:2
#Enter the number:4
#Enter the number:5
#Enter the number:1
#[2, 4, 5, 1]
#reversed list: [1, 5, 4, 2]