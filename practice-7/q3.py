def perimeter(h,w):
   tmp= h*2+w*2
   return tmp
def area(h,w):
    tmp=h*w;
    return tmp;
def create(h,w):
    for j in range(w):
        print()
        for i in  range(h):
            
            print("*",end=" ")
            
            

h=int(input("please enter rectangles height:"))
while not(h>=0):
    h=int(input("please enter rectangles height:"))
w=int(input("please enter rectangles width:"))
while not(w>=0):
    w=int(input("please enter rectangles width:"))
print()
print("area",area(h,w))
print("perimeter=",perimeter(h,w))
create(h,w)
    