n=int(input("please enter a number of token:"))
print("Toatal num of token      Tokens per turn      Turn no")
print("=====================================================")
x=2
i=1
while(n-x>0):
    print(n,"                      ",x,"                   ",i)

    n=n-x
    x=2*2**i

    i+=1
    
print("The las turn is:",i,"....")