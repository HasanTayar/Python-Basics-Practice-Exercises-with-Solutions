
n=int(input("enter How Many Students:"))
x=int(input("how many Errors:"))
cnt=0
for i in range(n):
    if(x<=3):
        cnt+=1
print("Number of passes is",cnt)
print("100% passes:",(cnt*n)/100)   
