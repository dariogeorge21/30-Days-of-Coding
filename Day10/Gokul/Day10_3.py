#Given the tuple t = ((1, 2), (3, 4), (5, 6)), write a program to calculate the sum of all the elements.
tuple1=((1, 2), (3, 4), (5, 6))
list1=list(tuple1)
new_list=[]

for tup in tuple1:
    for i in tup:
        new_list.append(i)
sum=0
for x in new_list:
    sum+=x
print("The sum is",sum)

#The sum is 21