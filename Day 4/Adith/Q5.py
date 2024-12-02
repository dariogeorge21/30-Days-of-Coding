a=int(input("eneter the number:"))
b=int(input("enter the second number:"))
if a<b:
    i=a
    while i<=b:
        iii=i
        count=0
        while iii>0:
            count+=1
            iii=iii//10
        ii=i
        arm=0
        while ii>0:
            digits=ii%10
            ar=digits**count
            arm+=ar
            ii=ii//10
        if arm==i:
            print(arm)
        i+=1
    
else:
    i=b
    while i<=a:
        iii=i
        count=0
        while iii>0:
            count+=1
            iii=iii//10
        ii=i
        arm=0
        while ii>0:
            digits=ii%10
            ar=digits**count
            arm+=ar
            ii=ii//10
        if arm==i:
            print(arm)
        i+=1
    
    
'''output
eneter the number:1000
enter the second number:1
1
2
3
4
5
6
7
8
9
153
370
371
407'''
