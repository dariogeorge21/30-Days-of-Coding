#Q3.WAP to print day of week 
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
x=int(input("Enter the number :"))
if x>0:
    print(day[x-1])
else:
    print("SOMETHING WENT WRONG")
