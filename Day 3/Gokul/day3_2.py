## Question 2: Write a program that determines if a given year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, unless it is divisible by 400.

year=int(input("Enter the number:"))

if year%4==0:
    if year%100!=0 or year%400==0: 
       print(f"{year} is a leap year")
       
    else:print(f"{year} is not a leap year")
        
else:
    print(f"{year} is not a leap year")
    
#Enter the number:2016
#2016 is a leap year

#Enter the number:1600
#1600 is a leap year

#Enter the number:1800
#1800 is not a leap year