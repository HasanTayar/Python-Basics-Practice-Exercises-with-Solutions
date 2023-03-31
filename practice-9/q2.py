def check( l ):
    for i in l:
        if l [ i ] == l[ i + 1 ]:
            return True
        else:
            return False
l =  []
N = 7
for i in range( N ):
    num = int( input("Please Enter A Numbers:"))
    l.append(num)
print(l)
if(check(l)):
    print("All The Element in The list are Eqauls")
else:
    print("The Element in The list Aren't Eqauls")
