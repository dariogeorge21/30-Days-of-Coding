#Write a program to print a pattern using a for loop
#Pattern :
#* * * *
#* * *
#* *
#*
#It must be a inversed right triangular pattern with with 4 no of rows

for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#output

#* * * *
#* * *
#* *
#*
