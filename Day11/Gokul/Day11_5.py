#**5. Write a program to find and return the common elements between two lists of integers. **
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
set1=set(list1)
set2=set(list2)
set3=set1.intersection(set2)
list3=list(set3)
print(list3)

#[4,5]
