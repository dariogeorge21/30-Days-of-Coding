#Question 2: Write a program that determines if a given year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, unless it is divisible by 400



Year=int(input("Enter the year:"))
if (Year%4==0) or(Year%400==0):
    print(Year,"is a leap year")
    
elif Year%100!=0:
    print(Year,"is not a leap year")
    
else:
    print(Year,"is not a leap year")
    
            #OUTPUT
            
 #  Enter the year:2017
 #2017 is not a leap year

 #[Program finished]