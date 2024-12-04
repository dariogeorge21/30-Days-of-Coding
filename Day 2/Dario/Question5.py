a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("=== Arithmetic Operations Menu ===")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice=int(input("Enter your choice: "))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
elif choice==5:
    print(a%b)
else:
    print("Wrong Input!!")