def fact(n):                 #creating a new function for factorial
    if n==0:                 #specifying case at 0
        return 1
    else:                    #using recurring functions
        return n*fact(n-1)
   

n = int(input("Enter the number for factor"))

print(fact(n))