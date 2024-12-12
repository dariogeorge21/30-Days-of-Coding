n=int(input("Enter the number:"))

if n>0 and n%2==0:
    print(f"{n} is positive and even")
    
elif n>0 and n%2!=0:
    print(f"{n} is positive and odd")
    
elif n<0 and n%2==0:
    print(f"{n} is negative and even")
    
elif n<0 and n%2!=0:
    print(f"{n} is negative  and odd")

else:
    print("Zero")
