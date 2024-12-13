 def reverse_string(s):
    if len(s) == 0:  # Base case
        return ""
    return reverse_string(s[1:]) + s[0]  # Recursive case

# Test
print(reverse_string("hello"))  # Output: "olleh"
