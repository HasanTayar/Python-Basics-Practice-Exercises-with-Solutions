a=str(input("Enter a Litter:"))
b=str(input("Enter a Litter: "))
c=str(input("Enter a Litter:"))
if ord(a)+1==ord(b) and ord(b)+1==ord(c):
    x=ord(c)+1
    print(chr(x))
else:
 print("Nope...Try Again")