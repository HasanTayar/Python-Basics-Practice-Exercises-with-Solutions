
def sumOfd(num):
    tmp=num
    sum=0
    while(tmp!=0):
        sum+=tmp%10
        tmp//=10
    return sum
def check(num):
    tmp=sumOfd(num)
    if tmp>9:
        tmp=sumOfd(num)
    while tmp!=3:
        tmp-=3
    if tmp==3:
        print("the num is %3==0",num)
        return True
    else:
        print("the num is not %3==0",num)
        return False
def main():
    num=int(input("Enter a number:"))
    tmp=check(num)
    print(tmp)
main()
