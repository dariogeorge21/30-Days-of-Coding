tuple1=(1,2,3)
tuple2=(4,5,6)
new_tuple=tuple1+tuple2
list1=list(new_tuple)
list1.sort(reverse=True)
print(tuple(list1))
