#3. Write a program to print all the prime numbers between two given numbers.

start=int(input("Enter the start:"))
end=int(input("Enter the end:"))

for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
        
    else:
        print(i,end=" ")
      
#Enter the start:2
#Enter the end:50
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47    
