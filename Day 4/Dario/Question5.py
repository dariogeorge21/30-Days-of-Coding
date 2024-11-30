num=int(input("Enter a number: "))
num_temp=num
arm_num=0
length=len(str(num))
while num>0:
    digit=num%10
    arm_num+=digit**length
    num=num//10
if arm_num==num_temp:
    print("It is a Armstrong Number")
else:
    print("It is not a Armstrong Number")