def flatten(nested_list):
    nlist=[]
    for i in nested_list:
        nlist.extend(i)
    return nlist
nested_list=[[1,2],[34,54]]
s=flatten(nested_list)
print(s)