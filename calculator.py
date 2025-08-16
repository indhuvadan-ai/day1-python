n1= float(input("enter your 1st number"))
n2= str(input("enter your operator"))
n3= float(input("enter your 2nd number"))

if n2=="+":
    print(n1+n3)

elif n2=="-":
    print(n1-n3)

elif n2=="*":
    print(n1*n3)

elif n2=="/":
    print(float(n1/n3))

elif n2=="%":
    print(n1%n3)

elif n2=="//":
    print(n1//n3)

else:
    print("Invalid operator")
