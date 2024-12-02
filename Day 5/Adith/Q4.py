n=input("enter the word:")
l=len(n)
reverse=""
for i in range(1,l+1):
    reverse=reverse+n[-i]
print(reverse)
    