#Write a recursive function to return the nth Fibonacci number

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))

#8