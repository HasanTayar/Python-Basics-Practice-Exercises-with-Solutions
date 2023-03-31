
x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
max=0
sum=0
z=0
a=0
while x%2==0 and y%2==0 or x%2==1 and y%2==1:
    if(sum<x+y):
        sum=x+y
        z=x
        a=y
    max+=1 
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:")) 
    
    
print("the couple which its  sum  is  the  biggest:",z,a)
print("number  of  couples:",max)


