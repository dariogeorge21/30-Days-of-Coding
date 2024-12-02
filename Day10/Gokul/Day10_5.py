#Write a program to remove all duplicate elements from the tuple (1, 2, 2, 3, 4, 4, 5) and return a new tuple.
tuple1=(1, 2, 2, 3, 4, 4, 5)
set1=set(tuple1)
print(tuple(set1))

#(1, 2, 3, 4, 5)