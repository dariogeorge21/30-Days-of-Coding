n=int(input("enter the number:"))
count=0
while n>0:
    count+=1
    n=n//10
print(f"the number of digits is {count}")