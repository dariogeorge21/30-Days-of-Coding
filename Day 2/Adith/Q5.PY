import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
} 

a=input("enter your operator:")
if a in ops:
    b=int(input("enter the number:"))
    c=int(input("enter the second number:"))
    d=ops[a](b,c)
    print(d)
else:
    print("try , * , + , - , / , operators ")

'''output__
enter your operator:*
enter the number:5 
enter the second number:9
45'''