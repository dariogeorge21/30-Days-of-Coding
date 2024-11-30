#Create a program to remove an element from a set if it exists.
set1={1,4,7,8,9}
print(set1)
num=int(input("Enter the element you want to remove:"))

if num in set1:
    set1.remove(num)
    print(set1)
else:
    print("not found")


#Enter the element you want to remove:7
#{1, 4, 8, 9}

E#nter the element you want to remove:2
#not found