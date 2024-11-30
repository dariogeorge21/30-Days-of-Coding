a=int(input("enter the number of chocolates:"))
b=int(input("enter the number of people:"))
if a>b :
    print(f"divide  {a//b} number of chocolates among each people.we get {a%b} remainder chocolates.")
else:
    print("insufficient chocolate")