#Convert the tuple (10, 20, 30, 40) into a list inside list where each list contains the value with its index.

tuple1=(10,20,30,40)
list1=list(tuple1)
new_list=[]
for i in list1:
    result=[i,list1.index(i)]
    new_list.append(result)
print(new_list)


#[[10, 0], [20, 1], [30, 2], [40, 3]]