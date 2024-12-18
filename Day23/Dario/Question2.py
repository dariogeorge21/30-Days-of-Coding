
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common_elements = list(set(list1) & set(list2))
print(f"Common Elements: {common_elements}")
