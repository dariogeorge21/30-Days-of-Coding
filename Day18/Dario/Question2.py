a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
adith=[]

for eldhose in range(a,b+1):
    johan=True
    for ben in range(2,eldhose):
        if eldhose%ben==0:
            johan=False
            break
    if johan==True:
        adith.append(eldhose)
            
print(adith)
