#Question 2 : Write a program to find wheather the number is odd or even? 

num=int(input("Enter the number:"))
if num==0:
    print(f"{num} is neither odd nor even ")
elif num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
#Enter the number:2
#2 is even