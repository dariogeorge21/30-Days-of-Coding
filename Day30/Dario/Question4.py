def first_recurring_character(string):
    s=set() 
    for char in string:
        if char in s:  
            return char
        s.add(char) 
    
    return None 

input_string = "abcdefgac"
result = first_recurring_character(input_string)
if result:
    print(f"The first recurring character is: {result}")
else:
    print("No recurring character found.")
