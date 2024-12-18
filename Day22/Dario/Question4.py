def remove_vowels(string):
    vowels = "aeiouAEIOU" 
    return ''.join(char for char in string if char not in vowels)

input_string = "The quick brown fox jumps over the lazy dog."
result = remove_vowels(input_string)
print(f"String without vowels: {result}")
