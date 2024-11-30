#Write a program to print Floyd's Triangular pattern using a for loop
#Pattern :
#1
#2 3
#4 5 6
#7 8 9 10
#It must be a right angled triangular pattern with 4 no. of rows
val=1
for i in range(4):
    for j in range(i+1):
        print(val,end=" ")
        val+=1
        
    print()
#1 
#2 3
#4 5 6
#7 8 9 10