x=int(input("Enter"))
if x%2==0:
	print(x)
	while x>2:
		print(x-2)
		x=x-2
if x%2!=0 and x>1:
	y=x-1
	print(y)
	while y>2:
		print(y-2)
		y=y-2