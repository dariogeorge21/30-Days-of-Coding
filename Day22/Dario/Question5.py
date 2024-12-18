def union_of_sets(set1, set2):
    """
    Find the union of two sets.
    :param set1: First set
    :param set2: Second set
    :return: A set containing the union of set1 and set2
    """
    return set1 | set2  
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_result = union_of_sets(set_a, set_b)
print(f"Union of {set_a} and {set_b}: {union_result}")
