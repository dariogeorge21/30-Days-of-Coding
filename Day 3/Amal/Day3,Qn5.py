#Question 5: Write a program that takes an integer and classifies it as:

#Positive and Even
#Positive and Odd
#Negative and Even
#Negative and Odd
#Zero

n=int(input("enter the number:"))

if n>0 and n%2==0:
    print(n,"is positive and even number")
    
elif n>0 and n%2!=0:
    print(n,"is postive and odd number")
   
elif n<0 and n%2==0:
    print(n,"is negative and even number")
    
elif n<0 and n%2!=0:
    print(n,"is negative and odd number")
    
      #OUTPUT
      
 #enter the number:71
#71 is postive and odd number

#[Program finished]