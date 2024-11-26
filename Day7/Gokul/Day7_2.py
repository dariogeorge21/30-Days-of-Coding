#Write a program to print Triangular pattern using a for loop
#Pattern :
#A
#A B
#A B C
#A B C D
#It must be a right triangular pattern with 4 rows and alphabets increasing in ascending order

for i in range(5):
	for j in range(i):
		print(chr(65+j),end=" ")
	print()

#output
#A
#A B
#A B C
#A B C D

