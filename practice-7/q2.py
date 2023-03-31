def check(d,p):
    flag1=0
    flag2=0
    if p>7:
        flag1=1
    if d==3 and p<4:
        flag2=1
    return flag1,flag2
####################################################################################################################
cnt1=0
cnt2=0
for i in range(1,6):
    d=int(input("please enter the day in the week:"))
    while not (d >=1 and d<=7):
        d=int(input("please enter the day in the week:"))
    p=int(input("please enter the Pollution level from 1 to 10 :"))
    while not(p>=1 and p<=10):
         p=int(input("please enter the Pollution level from 1 to 10 :"))
    f1,f2=check(d,p)
    if(f1==1):
        cnt1+=1
    if(f2==1):
        cnt2+=1
print("Number of days when an infection level was greater than 7 : ",cnt1)
print("Number of Tuesdays where pollution level was less than 4 :",cnt2)


