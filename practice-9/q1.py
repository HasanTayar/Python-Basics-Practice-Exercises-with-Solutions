
def shift(list,n):
    return list[n:]+list[:n]
N=5
l=[]
for i in range(N):
    number=int(input("PLease Enter A numbers in Array:"))
    l.append(number)
l2=shift(l,-1)
print("The Orginal list:")
print(l)
print("The new List is:")
print(l2)

    
