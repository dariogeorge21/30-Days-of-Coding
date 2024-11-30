#Write a menu driven
# program by asking the user to perform which 
# arithmetic operator has to be used, and perform it by inputing 2 numbers
x =int(input("Enter the number :"))
y=int(input('Enter the number :'))
l=['+','*','/','-']
print('+=1,','*=2,','/=3,','-=4')
z=int(input('Enter'))
a=l[z-1]
if a==l[0]:
	print(x+y)
if a==l[1]:
	print(x*y)
if a==l[2]:
	print(x/y)
if a==l[3]:
	print(x-y)
		
		