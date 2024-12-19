string="A man, a plan, a canal, Panama!"
string_without="".join([char for char in string if char.isalnum()])
string_lower=string_without.lower()

reverse=string_lower[::-1]
if reverse==string_lower:
	print("True")
else:
	print("False")
  
