def sum(w1,w2):
    sum=0
    sum2=0
    for i in w1:
        sum+=i
    avg=sum/7
    for i in w2:
        sum2+=i
    avg2=sum2/7
    print("Disconects Average for First Week:",avg)
    print("Disconects Average for Second Week:",avg2)
    if avg2-avg>=25:
        print("Great")
    else:
        print("Nope")

def main():
    D=7
    w1=[]
    w2=[]
    for i in range(D):
        days=int(input("PLease Enter Number Disconectds for week 1:"))
        w1.append(days)
    for i in range(D):
        days2 = int(input("Please Enter Number Disconecteds for week 2:"))
        w2.append(days2)
    sum(w1,w2)
main()


