# Introduction to Programming Using Python

Hello Team,
This folder contains questions and its solutions to basic programming problems for **Day 1**.
Since it is the first day you will be provided with the solutions in case if you wish to refer.

---

## Question 1: Write a program to find the sum of 2 numbers.

```python
# Program to find the sum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}.")
```
---
## Question 2: Write a program to find wheather the number is odd or even?
---
```python
# Program to check if a number is odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```
---
## Question 3 : Write a program to print week of day when a week number is given as input? ( Take Monday as 1)
---

```python
# Program to print the day of the week
week_number = int(input("Enter the week number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= week_number <= 7:
    print(f"The day of the week is {days[week_number - 1]}.")
else:
    print("Invalid week number! Please enter a number between 1 and 7.")
```
---
## Question 4 : Write a program to equally divide N no of chocolates among X no of people? Also show the remaining no of chocolates?
---
```python

# Program to equally divide chocolates among people
total_chocolates = int(input("Enter the total number of chocolates: "))
total_people = int(input("Enter the number of people: "))

if total_people == 0:
    print("Cannot divide chocolates among zero people!")
else:
    chocolates_per_person = total_chocolates // total_people
    remaining_chocolates = total_chocolates % total_people

    print(f"Each person gets {chocolates_per_person} chocolates.")
    print(f"Remaining chocolates: {remaining_chocolates}")
```
---
## Question 5 : Write a program to find the square of the smallest numbers among 3 numbers as input from user?
---
```python

# Program to find the square of the smallest number among three inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

smallest = min(num1, num2, num3)
square = smallest ** 2

print(f"The smallest number is {smallest}, and its square is {square}.")

```
---



