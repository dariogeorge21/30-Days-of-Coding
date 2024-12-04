# Recursion using Python **Day 15**

This folder contains a list of Python programming questions focused on **recursion**. Each question includes a brief description and a hint to help you get started.

---

## 1. Factorial Calculation
Write a recursive function to calculate the factorial of a given number.

**Example**:  
Input: `5`  
Output: `120`  

**Hint**:  
The factorial of `n` is `n * factorial(n-1)`, and the base case is `factorial(0) = 1`.

---

## 2. Fibonacci Sequence
Write a recursive function to return the `n`th Fibonacci number.

**Example**:  
Input: `6`  
Output: `8`  

**Hint**:  
The `n`th Fibonacci number is `fib(n-1) + fib(n-2)`, with base cases `fib(0) = 0` and `fib(1) = 1`.

---

## 3. Sum of Digits
Write a recursive function to find the sum of the digits of a given number.

**Example**:  
Input: `123`  
Output: `6`  

**Hint**:  
Take the last digit using `% 10`, add it to the sum of the rest of the digits (`num // 10`), and stop when the number is `0`.

---

## 4. Reverse a String
Write a recursive function to reverse a string.

**Example**:  
Input: `"hello"`  
Output: `"olleh"`  

**Hint**:  
Remove the first character and append it at the end of the reversed version of the rest of the string.

---

## 5. Power Calculation
Write a recursive function to calculate `x^n` (x raised to the power n).

**Example**:  
Input: `x = 2, n = 3`  
Output: `8`  

**Hint**:  
Use `x * power(x, n-1)` and stop when `n = 0` (return `1`).

---

Feel free to attempt these problems and refer to the hints if you get stuck!
Thankyou and have a nice day!!
