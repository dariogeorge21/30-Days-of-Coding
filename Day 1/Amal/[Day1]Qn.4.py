Question 4 : Write a program to equally divide N no of chocolates among X no of people? Also show the remaining no of chocolates?

ch=int(input("Enter the number of  chocolates:"))

p=int(input("Enter the number of people:"))

d=float(ch/p)
k=int(ch/p)
e=int(ch-(k*p))



if d%2==0:
    print("Each person gets",k, "chocolates")
    print("remaining chocolates is 0")
    
else:
      print("Each person gets",k, "chocolates")
      print(" The remaining  number of chocolate is",e) 
      

          𝗢𝗨𝗧𝗣𝗨𝗧


Enter the number of  chocolates:27
Enter the number of people:2
Each person gets 13 chocolates
 The remaining  number of chocolate is 1

Enter the number of  chocolates:100
Enter the number of people:5
Each person gets 20 chocolates
remaining chocolates is 0

[Program finished]