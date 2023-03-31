thisYear=int(input("Enter Year"))
yearB=int(input("BirthYear for students:"))
cnt1=0
cnt2=0
cnt3=0
while yearB>=0:
    if (thisYear-yearB)==17:
        cnt1+=1
    if (thisYear-yearB)==16:
        cnt2+=1
    if (thisYear-yearB)==15:
        cnt3+=1   
    yearB=int(input("BirthYear for students:"))            
print("The Student that there Age are 17:",cnt1)  
print("The Student that there Age are 16:",cnt2)
print("The Student that there Age are 15:",cnt3)
if(cnt1+cnt2+cnt3)==3:
    print("Ok")    