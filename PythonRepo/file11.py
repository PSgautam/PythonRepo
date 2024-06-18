#To generate first n numbers in Fabonacci sequence
num=int(input("Enter a number"))
list=[]
a=0
b=1
for i in range(num):
    list.append(a)
    c=a+b
    a=b
    b=c
print(list)
        
    