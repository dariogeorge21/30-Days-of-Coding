#Write a Python program to create a set and #add elements to it.
set1= set()
limit=int(input("Enter the limit:"))
for i in range(limit):
     n=int(input("Enter the number:"))
     set1.add(n)
print(set1)

#Enter the limit:4
#Enter the number:1
#Enter the number:6
#Enter the number:10
#Enter the number:7
#{1, 10, 6, 7}
