list1= [[0,0],
        [0,0],
        [0,0]];
for i in range(0,3):
    for y in range(0,2):
        list1[i][y]=int(input("enter num"));
print(" ")
print("Matrix A");
for i in range(0,3):
    for y in range(0,2):
        print(list1[i][y],end=" ");
    print()
list2=[0,0,0];
print(" ");
print("Matrix B");
for i in range(0,3):
    sum=0;
    for y in range(0,2):
        sum=sum+list1[i][y];
        list2[i]=sum;
for i in range(3):
    print(list2[i],end=" ");
list3=[0,0];
for i in range(0,2):
    sum=0;
    for y in range(0,3):
        sum=sum+list1[y][i];
        list3[i]=sum;
print(" ");
print("Matrix C");
for i in range(0,2):
    print(list3[i],end=" ");