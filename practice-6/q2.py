def afterp(num):
    flag=0
    if num < 0 :
        num = num * -1 
        flag=1
    if num%2 > 1 :
        a = num%2-1
    else :        
        a=num%2
    if flag == 0 :
        return num - a 
    else :
        return (num - a) * -1
def main():
    num=float(input("Enter a Float Number:"))
    tmp=afterp(num)
    print(tmp)
main() 