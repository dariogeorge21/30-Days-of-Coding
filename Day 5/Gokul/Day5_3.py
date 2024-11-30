
#Write a program to reverse a string using a for loop.

word=input("Enter the string:")
reverse=""

position=len(word)-1

for i in word:
    reverse=reverse+word[position]
    position=position-1
print(reverse)

#Enter the string:Python
#nohtyP