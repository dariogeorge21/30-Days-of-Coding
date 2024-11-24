sentence=str(input("Enter sentence: "))
sentence_list=sentence.split(" ")
words=0
for i in sentence_list:
    words+=1
print("No of words: ",words)