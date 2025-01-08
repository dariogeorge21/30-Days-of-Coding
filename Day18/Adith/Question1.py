def pali(string):
    string=string.lower()
    if string==string[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
