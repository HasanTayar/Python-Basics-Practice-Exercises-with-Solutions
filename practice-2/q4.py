import math
A=int(input("Enter A:"))
B=int(input("Enter B:"))
C=int(input("Enter C:"))
X=(B**2)-(4*A*C)
x1=(-B+math.sqrt(X))/(2*A)
x2=(-B-math.sqrt(X))/(2*A)
print("X1=",x1)
print("X2=",x2)


