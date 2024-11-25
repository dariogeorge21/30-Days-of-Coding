#Write a program to print Triangular pattern using a for loop
#Pattern :
#1 2 3 4
#1 2 3
#1 2
#1
#It must be a right triangular pattern with 4 rows and numbers increasing in ascending order

for i in range(4,0,-1):
    for j in range(i):
        print(1+j,end=" ")
    print()

#output
#1 2 3 4 
#1 2 3
#1 2
#1