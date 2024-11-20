total_chocolates = int(input("Enter the total number of chocolates: "))
total_people = int(input("Enter the number of people: "))

if total_people == 0:
    print("Cannot divide chocolates among zero people!")
else:
    chocolates_per_person = total_chocolates // total_people
    remaining_chocolates = total_chocolates % total_people

    print(f"Each person gets {chocolates_per_person} chocolates.")
    print(f"Remaining chocolates: {remaining_chocolates}")