tuple1=(10,20,30,40)
list1=list(tuple1)
new_list=[]
for i in list1:
    result=[i,list1.index(i)]
    new_list.append(result)
print(new_list)
