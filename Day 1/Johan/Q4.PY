#Q4.WAP to equally divide N no of chocolates among X no of people? Also show the remaining no of chocolates
n=int(input("Enter the number of people :"))
c=int(input("Enter the number of choclate :"))
x=c%n
y=c//n
print("Total number of chocalate each person got is :",y)
print("Chocalate remaining is :",x)