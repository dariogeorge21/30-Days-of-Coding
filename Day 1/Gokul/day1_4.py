#Question 4 : Write a program to equally divide N no of chocolates among X no of people? Also show the remaining no of chocolates?
choco=int(input("Enter the no of chocolates:"))
people=int(input("Enter the no of people:"))

if choco>=people:
    remain=choco%people
    equal=(choco-remain)//people

    print(f"We can give {equal} chocolates to each people")
    print(f"{remain} chocolates are remaining")

else:
    print("No sufficient chocolates to divide equally") 
    
#output
#Enter the no of chocolates:8
E#nter the no of people:6
#We can give 1 chocolates to each people
#2 chocolates are remaining

