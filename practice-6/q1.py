def even(num):
    cnt=0
    x=num
    while(x!=0):
        if x%10%2==0:
            cnt+=1
        x=x//10
    return cnt

n=int(input("enter a number for range:"))
max=0
x=0
tmp=0
for i in range(n):
    num=int(input("Enter a Number:"))
    x=even(num)
    if x>max:
        max=x
        tmp=num

print(tmp)
