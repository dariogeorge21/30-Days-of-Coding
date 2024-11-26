#Write a program to print Pyramid pattern using a for loop
#Pattern :
#                   * 
#                  ***
#                 ***** 
#                *******   
It must be a pyramid pattern with 4 rows and patterns increasing in ascending order


for i in range(1,9,2):
    for j in range(7-i,0,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()
    
output
#      *       
#    * * *     
#  * * * * *   
#* * * * * * * 