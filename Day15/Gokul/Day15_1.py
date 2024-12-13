#Write a recursive function to calculate the factorial of a given number.
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

#120