import math

def find_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Example usage
side_a = 3
side_b = 4
hypotenuse = find_hypotenuse(side_a, side_b)
print("The length of the hypotenuse is:", hypotenuse)
