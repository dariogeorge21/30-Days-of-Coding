num=int(input("Enter a number: "))
if num==0:
    print("The number is zero")
else:
    if num>0:
        if (num%2==0):
            print("Positive and Even")
        else:
            print("Positive and Odd")
    else:
        if num%2==0:
            print("Negative and Even")
        else:
            print("Negative and Odd")