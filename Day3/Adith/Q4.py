'''Write a program to check if three sides entered by the user can form a valid triangle.
 The triangle is valid if the sum of any two sides is greater than the third side.'''
a=[]
for i in range(3):
    b=int(input(f"enter the side{i+1}:"))
    a.append(b)
a.sort()
if a[0]+a[1]<=a[2]:
    print("the triangle can be made")
else:
    print("the triangle is not possible")