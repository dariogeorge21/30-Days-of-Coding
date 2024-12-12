
x=int(input('Enter the number'))
if x>0 and x%2==0:
	print('POSITIVE EVEN NUMBER')
elif x<0 and x%2==0:
	print('NEGATIVE EVEN NUMBER ')
elif x>0 and x%2!=0:
	print('POSTIVE ODD NUMBER')
elif x<0 and x%2!=0:
	print('NEGATIVE ODD NUMBER')	
else:
	print('0' ,'NOT INCLUDED')
