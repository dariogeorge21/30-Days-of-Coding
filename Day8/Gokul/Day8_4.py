#Write a program to count how many times a #specific element appears in a list.

list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)

count1=int(input("Enter the element:"))
list2=list1.count(count1)
print(f"Occurences of {count1} is", list2)

#Enter the limit:4
#Enter the number:1
#Enter the number:3
#Enter the number:2
#Enter the number:2
#Enter the element:2
#Occurences of 2 is 2
