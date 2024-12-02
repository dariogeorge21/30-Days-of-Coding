n=4
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
   
    for j in range(i+(i-1)):
        print("*",end="")
        
    print()