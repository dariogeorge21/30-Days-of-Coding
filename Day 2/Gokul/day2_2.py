#Question 2: Write a program to check weather the number X is a multiple of Y or not?

x=int(input("Enter the number X:"))
y=int(input("Enter the number Y:"))

if x%y==0:
    print(f"{x} is a multiple f {y}")

else:
    print("Not a multiple")
    
    
#Enter the number X:65
#Enter the number Y:5 
#65 is a multiple f 5