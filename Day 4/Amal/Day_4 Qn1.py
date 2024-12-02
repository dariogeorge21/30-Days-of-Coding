
#Print Even Numbers from N to 1
#Write a program to print all even numbers between (N) and 1, where (N) is input by the user.



# Input the value of N
N = int(input("Enter a number N: "))

# Print even numbers from N to 1
print("Even numbers from", N, "to 1:")

while N >= 1:
    if N % 2 == 0:
        print(N)
    N -= 1
    

#Enter a number N: 16
#Even numbers from 16 to 1:
#16
#14
#12
#10
#8
#6
#4
#2

#[Program finished]  