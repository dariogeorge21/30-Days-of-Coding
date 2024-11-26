#Write a program to print Pyramid pattern using a for loop
#Pattern :
#                   1 
#                  121
#                 12321 
#                1234321   
#It must be a pyramid pattern with 4 rows and patterns increasing in ascending order

for i in range(0,4):

    for l in range(4-i,0,-1):
        print(" ",end="")    
    
    for j in range(1,i+1):
        print(j,end="")

    for k in range(i+1,0,-1):
        print(k,end="")
    
    print()
    
#output
#    1
#   121
#  12321
# 1234321