def positive(n):
    if n>1:
       if n%2!=0:
          even=n-1

       else:
           even=n
    
    while even>1:
        print(even,end=" ")
        even=even-2
        
def negative(n):
    if n<1:
       if n%2!=0:
          even=n+1

       else:
           even=n
    
    while even<0:
        print(even,end=" ")
        even=even+2

n=int(input("Enter the number:"))
if n>1:
    positive(n)
else:
    negative(n)
    
###Positive even number as N
#Enter the number:14
#14 12 10 8 6 4 2 

###Positive odd number as N
#Enter the number:13
#12 10 8 6 4 2 

###Negative even number as N
#Enter the number:-18
#-18 -16 -14 -12 -10 -8 -6 -4 -2


###Negative odd number as N 
#Enter the number:-11
#-10 -8 -6 -4 -2





