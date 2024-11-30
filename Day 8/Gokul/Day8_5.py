#Write a Python program to check whether a given element exists in a list.
list1=[]
limit=int(input("Enter the limit:"))
for num in range(limit):
	num=int(input("Enter the number:"))
	list1.append(num)
 
common=int(input("Enter the element:"))
for j in list1:
    if j==common:
        print(True)
        break
else:
    print(False)
#Enter the number:3
#Enter the number:4
#Enter the number:5
#Enter the number:8
#Enter the element:8
#True


#Enter the limit:4
#Enter the number:1
#Enter the number:4
#Enter the number:6
#Enter the number:8
#Enter the element:0
#False