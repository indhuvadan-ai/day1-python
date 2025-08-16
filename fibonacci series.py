f1=0  #specify f1 and f2
f2=1
n=int(input("Enter the range of fibonacci series"))  #take input from the user
for i in range(n+1):                                 #useing for loop since we are dealing with range
    print(f1)
    
    temp=f1     #we took a temporary variable
    f1=f2       #f2 will become f1
    f2=temp+f1  #f2 will be the new sum of temporary variable and f1
    