


salary=int(input("Enter Salary:"))
month=int(input("Month:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    perday=salary/(31-8)
elif month!=2:
    perday=salary/(30-8)
elif month==2:
    perday=salary/(28-8)
print("Your Salary per Day:",perday)
