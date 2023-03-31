alphabet=str(input("Enter From A-Z:"))
if alphabet=='Z':
    print("The next Letter is:",chr('A'))
elif alphabet=='z':
 print("The next Letter is:",'a')
else:
    a=ord(alphabet)+1
    print("The next Letter is:",chr(a))
