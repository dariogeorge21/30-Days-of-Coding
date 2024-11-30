c=int(input("Enter the total number of chocolates: "))
p=int(input("Enter the number of people: "))

if c== 0:
    print("Cannot divide chocolates among zero people!")
else:
    a= c // p
    r = c % p

    print("Each person gets chocolates.",a)
    print("Remaining chocolates: ",r)