for i in range(3):
    grade=float(input("Enter Grades 40-100:"))
    while (grade<40 or grade>100) or (grade%2==0 or grade%2==1):
         grade=float(input("Only number from 40-100!:"))
    if grade%2>1:
        a=grade%2 -1
        if a>=0.5:
            print("The full grade is:",int(grade+(1-a)),",and the saved grade:","-","%.1f"%(1-a))
        else:
            print("The full grade is:",int(grade-a),",and the saved grade:","+","%.1f"%a)
    else:
        a=grade%2
        if a>=0.5:
           print("The full grade is:",int(grade+(1-a)),",and the saved grade:","-","%.1f"%(1-a))
        else:
            print("The full grade is:",int(grade-a),",and the saved grade:","+","%.1f"%a)

