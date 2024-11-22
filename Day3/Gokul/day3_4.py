## Question 4: Write a program to check if three sides entered by the user can form a valid triangle. The triangle is valid if the sum of any two sides is greater than the third side

tri=[]

for i in range(3):
    side=int(input("Enter the side:"))
    tri.append(side)
tri.sort

if (tri[0]+tri[1])>tri[2]:
    print("Valid Triangle")
else:
    print("Invalid triangle")    
    
#Enter the side:4
#Enter the side:5
#Enter the side:6
#Valid Triangle

#Enter the side:4
#Enter the side:5
#Enter the side:10
#Invalid triangle