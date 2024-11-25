#Write a program that takes a student's marks and prints the grade

a=int(input("enter the marks:"))
if a>=90:
    print("your grade is A")
elif 90>a>=80:
    print("your grade is B")
elif 80>a>=70:
    print("your grade is C")
elif 70>a>=60:
    print("your grade is D")
else:
    print("your garde is F")