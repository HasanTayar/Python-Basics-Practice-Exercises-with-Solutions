a,b=eval(input("Enter 2 number:"))
sum=0
cnt=0
a1=0
b1=0
while a%2==0 and b%2==0 or a%2==1 and b%2==1:
    if(sum<a+b):
        sum=a+b
        a1=a
        b1=b
    cnt+=1   
    a,b=eval(input("Enter 2 number:"))
print(a1,b1)
print(cnt)    