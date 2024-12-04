#Write a Python program that iterates using for loop over a list of integers and prints "Even" for even numbers and "Odd" for odd numbers.

n=int(input("Enter the limit:"))
list1=[]

for i in range(n):
    num=int(input("Enter the number:"))
    list1.append(num)

print(list1)

for j in list1:
    if j%2==0:
        print("Even",end=" ")
    else:
        print("Odd",end=" ")

#Enter the limit:4
#Enter the number:3
#Enter the number:2
#Enter the number:7
#Enter the number:11
#[3, 2, 7, 11]
#Odd Even Odd Odd      
