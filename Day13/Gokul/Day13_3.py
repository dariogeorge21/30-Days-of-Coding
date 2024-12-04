#Given the dictionary:
#student = {'name': 'John', 'age': 18, 'grade': 'A'}

#Write a function that removes the key 'grade' from the dictionary. Print the dictionary before and after removal.

student = {'name': 'John', 'age': 18, 'grade': 'A'}
print(student)

del student["grade"]
print(student)

#output
#{'name': 'John', 'age': 18, 'grade': 'A'}
#{'name': 'John', 'age': 18}

