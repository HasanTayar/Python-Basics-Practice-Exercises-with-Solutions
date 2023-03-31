N=5
sums = [0]*N
show=int(input("Please enter the number of the show you want 1-5: "))
while show!=0:
    show=int(input("Please enter again the number of the show you want 1-5: "))
    if show==0:
        break
    while not (show>=1 and show<=5):
        show=int(input("Please enter the number of the show you want 1-5: "))
    tickits=int(input("please enter number of tickets you want: "))
    sums[show-1]+=tickits
for i in range (N):
    print("show no",(i+1),"number of tickets",sums[i])
max1 = sums[0]
max2 = sums[0]
ind = 0
ind2 = 0
for i in range(N):
    if sums[i] > max1:
        max1 = sums[i]
        ind = i+1
for i  in range(N):
    if sums[i] > max2 and max2 != max1:
        max2 = sums[i]
        ind2 = i+1
print("The Most Requerd Show:",ind,ind2)





    




    


