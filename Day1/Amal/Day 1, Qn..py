#Question 3 : Write a program to print week of day when a week number is given as input? ( Take monday as 1)

week_number = int(input("Enter the week number (1-7): "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= week_number <= 7:
    print(f"The day of the week is {days[week_number - 1]}.")

else:
    print("Something Wrong! Try again.")


             𝗢𝗨𝗧𝗣𝗨𝗧


Enter the week number (1-7): 5
The day of the week is Friday.

[Program finished]