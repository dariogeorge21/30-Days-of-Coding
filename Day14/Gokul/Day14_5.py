#Write a function named greet_person() that takes a person's name as a parameter and prints a greeting. If no name is provided, the function should use "Guest" as the default name
	
def greet(name="Guest"):
	print("Hello,",name+"!")
    
greet("John")
greet()

#Hello, John!
#Hello, Guest!
