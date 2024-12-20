#Write a program to print diamond pattern using a for loop

n=5
#for first part 
for i in range(1,n+1):
    #for space
    for j in range(n-i,0,-1):
        print(" ",end="")
    #for space
    for j in range(1,2*i):
        print("*",end="")
    print()
    
#for second part
for k in range(n,0,-1):
    for l in range((n+1)-k):
        
        print(" ",end="")
    for l in range(2*k-3,0,-1):
        print("*",end="")
    print()
    
'''*
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''

