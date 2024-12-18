
string = "Hello, World! How are you?"
vowels = "aeiouAEIOU" 
count = 0
    
for char in string:
    if char in vowels:  # Check if the character is a vowel
            count += 1

print(f"Number of vowels: {count}")
