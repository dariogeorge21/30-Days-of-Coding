
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result=(set1 - set2) | (set2 - set1)

print(f"Symmetric Difference: {result}")