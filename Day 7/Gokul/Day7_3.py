#Write a program to print Triangular pattern using a for loop
#Pattern :
#A B C D
#A B C
#A B
#A
#It must be a inversed right triangular pattern with 4 rows and alphabets decreasing in descending order

for i in range(4,0,-1):
	for j in range(i):
		print(chr(65+j),end=" ")
	print()
#output
#A B C D
#A B C
#A B
#A


