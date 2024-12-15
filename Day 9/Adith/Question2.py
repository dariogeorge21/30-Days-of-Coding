set1={1,4,7,8,9}
print(set1)
num=int(input("Enter the element you want to remove:"))

if num in set1:
    set1.remove(num)
    print(set1)
else:
    print("not found")
