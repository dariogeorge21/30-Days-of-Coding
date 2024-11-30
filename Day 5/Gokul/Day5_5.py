#Create a program to count the number of words in a sentence using a for loop

word=input("Enter the string:")

list1=word.split(" ")
count=0

for i in list1:
    count=count+1
print("The number of words is",count)

#Enter the string:I am Iron Man
#The number of words is  4