x=int(input("Enter :"))
sum=0
while x>0:
	sum=x%10+sum
	x=x//10
print(sum)