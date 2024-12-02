n=4
for i in range(1,n+1):
    a=1
    for k in range(n-i):
        print(" ",end="")
   
    for j in range(i):
        print(a,end="")
        a+=1
    a-=1
    for l in range(i-1):
        a-=1
        print(a,end="")    
    
    print()