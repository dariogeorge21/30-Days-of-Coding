week_number = int(input("Enter the week number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= week_number <= 7:
    print(f"The day of the week is {days[week_number - 1]}.")
else:
    print("Invalid week number! Please enter a number between 1 and 7.")