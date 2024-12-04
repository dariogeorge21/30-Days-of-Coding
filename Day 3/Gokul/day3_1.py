##Question 1: Write a program that takes a student's marks and prints the grade based on the following criteria:  
#- Marks > 90: `A`  
#- Marks > 80: `B`  
#- Marks > 70: `C`  
#- Marks > 60: `D`  
#- Otherwise: `F`  

mark=int(input("Enter the number:"))

if mark>=90:
    print("You have A grade")
elif mark>=80:
    print("You have B grade")
elif mark>=70:
    print("You have C grade")
elif mark>=60:
    print("You have D grade")
else:
    print("You have F grade")