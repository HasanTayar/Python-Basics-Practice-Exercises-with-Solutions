def func(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i*j==num:
                print("(",i,",",j,")",end="")
##################################################################################                
num=int(input("Please Enter a Number:"))
func(num)
j=0
i=0
while i<=num and j<=num:
    if i*j==num:
        print("(",i,",",j,")",end="")
    if(i==num):
        j+=1
        i=0
    i+=1

    

 