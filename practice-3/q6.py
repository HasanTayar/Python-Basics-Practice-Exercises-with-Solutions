num1=int(input("Enter a Number:"))
num2=int(input("Enter a Number:"))
if (num1%10==num2//10 and num1//10==num2%10) or num1==num2: 
  print("the number is same digits:",num1,num2)
else:
  print("Nope...")