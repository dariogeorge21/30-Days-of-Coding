#Question 3: Write a program to find the smallest of three numbers entered by the user.

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the Third number:"))

if x<y and x<z:
    print(x,"is the smallest numer")
    
elif y<x and y<z:
     print(y,"is the smallest number")
     
else:
     print(z,"is the smallest number")
     
     
      #OUTPUT
    
 #Enter the first number:17
#Enter the second number:5
#Enter the Third number:100
#5 is the smallest number

#[Program finished]