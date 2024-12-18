def generate_subsets(s):
    subsets = []
    n = len(s)
    
    # Iterate through all numbers from 0 to 2^n - 1
    for i in range(2 ** n):
        subset = []
        # For each bit position, check if it is set (1)
        for j in range(n):
            if (i >> j) & 1:
                subset.append(s[j])
        subsets.append(subset)
    
    return subsets

# Example usage
s = ['a', 'b', 'c']
subsets = generate_subsets(s)
print(subsets)
