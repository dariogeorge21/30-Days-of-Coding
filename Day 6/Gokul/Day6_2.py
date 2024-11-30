
##Write a program to print a pattern using a for loop
#Pattern :
#*
#* *
#* * *
#* * * *
#It must be a right triangular pattern with 4 no of rows

for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
        
#output

#* 
#* *
#* * *
#* * * *