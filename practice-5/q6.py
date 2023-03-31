cnt=0
sum=0
for i in range(1,1001):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        cnt+=1
        print("perfect number is:",i)
print("The Counter is:",cnt)