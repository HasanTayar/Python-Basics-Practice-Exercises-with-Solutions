for i in range(7):
    n=int(input("Enter a 3 digts number:"))

    if n<100 or n>999:
        print("the number hasn't a 3-digits")
    
    else:
        if(n%10 != n//10%10 and n%10 != n//100 and n//100 !=n//10%10):
            print("The number has a diffrent digtis",n)
        
        else:
            print("the number has at least two same digits")
