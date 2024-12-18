def replace_substring(original_string, old_substring, new_substring):
    return original_string.replace(old_substring, new_substring)

# Example usage
original_string = "Hello, world! Welcome to the world of Python."
old_substring = "world"
new_substring = "universe"

result = replace_substring(original_string, old_substring, new_substring)
print("Updated string:", result)
