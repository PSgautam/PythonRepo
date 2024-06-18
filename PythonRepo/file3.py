#Factorial of a given number
n=int(input("Enter a number:"))
a=n
fact=1
if n==1 or n==0:
    print("factorial of ",n," is 1")
elif n<0:
    print("factorial not exist")
else:
    while(n>0):
        fact*=n
        n-=1    
    print("factorial of ",a," is ",fact) 
    
