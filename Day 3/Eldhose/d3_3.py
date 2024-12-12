small=[]

for i in range(3):
    n=int(input("Enter the number:"))
    small.append(n)
small.sort()
print(f"The smallest number is {small[0]}")
