#Write a program to find the union, intersection, and difference between two sets.

set1={1,2,3}
set2={3,4,5}

print("Union=",set1|set2)# or set1.union(set2)
print("Intersection=",set1&set2)#or set1.difference(set2)
print("Symmetric difference=",set1.symmetric_difference(set2))#or set1^set2

#Union= {1, 2, 3, 4, 5}
#Intersection= {3}
#Symmetric difference= {1, 2, 4, 5}