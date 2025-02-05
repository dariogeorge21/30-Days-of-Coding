n=4
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(1,i+2):
        print(j,end=" ")
    for j  in range(i,0,-1):
        print(j,end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    for j  in range(n,i+1,-1):
        print(j,end=" ")
    print()