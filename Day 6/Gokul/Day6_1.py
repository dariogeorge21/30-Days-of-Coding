#Write a program to print a pattern using a for loop
#Pattern :
#* * * *
#* * * *
#* * * *
#* * * *
#It must be a square pattern with equal no of rows (4) and columns

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()

#output
#* * * * 
#* * * * 
#* * * * 
#* * * * 