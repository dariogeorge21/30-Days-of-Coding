x=int(input('Enter the year'))
if x%4==0 and x%400==0 and x%100==0:
	print (x,'IS A LEAP YEAR')
elif x%4==0 and x%100!=0:
	print (x,'IS A LEAP YEAR')
else:
	print(x,'NOT A LEAP YEAR')
