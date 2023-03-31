import math
A=int(input("Enter A Deg:"))
B=int(input("Enter A Deg:"))
C=int(input("Enter A Deg:"))
S=(A+B+C)/2
if(A+B>C) or(A+C>B)or(B+C>A):
    area=math.sqrt(S*(S-A)*(S-B)*(S-C))
    print("area:",area)
else:
 print("Erorr")
    