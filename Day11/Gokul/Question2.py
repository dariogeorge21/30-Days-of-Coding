#Given a list of integers, write a program to remove all duplicates and return the second largest unique number.

list1=[5, 3, 9, 3, 5, 7, 9]

set1=set(list1)
list2=list(set1)
list2.sort()
print("Second largest unique number:",list2[-2])

#Second largest unique number: 7

