#Question 4: Write a program to check if three sides entered by the user can form a valid triangle. The triangle is valid if the sum of any two sides is greater than the third side.

AB=int(input("Enter the length of first side (AB):"))
BC=int(input("Enter the length of second side(BC):"))
AC=int(input("Enter the length of third side(AC):"))

sum1=(AB+BC)
sum2=(BC+AC)
sum3=(AC+AB)

if sum1>AC:
    print("The triangle is valid")
    
else:
    print("The triangle is not  valid")

        #OUTPUT
 
 #Enter the length of first side (AB):3
#Enter the length of second side(BC):8
#Enter the length of third side(AC):7
#The triangle is valid

#[Program finished] 