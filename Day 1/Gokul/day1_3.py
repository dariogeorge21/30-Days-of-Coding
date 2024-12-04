#Question 3 : Write a program to print week of day when a week number is given as input? ( Take Monday as 1)

n=int(input("Enter the day:"))

match n:
    case 1:
        print("Monday")
           
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday") 
    case 5:
        print("friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")

#output

#Enter the day:2
#Tuesday