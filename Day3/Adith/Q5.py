'''Write a program that takes an integer and classifies it as:
Positive and Even
Positive and Odd
Negative and Even
Negative and Odd
Zero'''

a=int(input("enter the number:"))

if a<0:
    if a%2==0:
        print(f"the enetered value {a} is negative and even")
    else:
        print(f"the enetered value {a} is negative and odd")
elif a>0:
    if a%2==0:
        print(f"the enetered value {a} is positive and even")
    else:
        print(f"the enetered value {a} is positive and odd")
else:
    print("the number is zero")