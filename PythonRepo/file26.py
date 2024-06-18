#To check if a string starts with a given prefix or ends with a given suffix
string=input("Enter a string:")
length=len(string)
prefix=input("Enter a prefix character:")
suffix=input("Enter a suffix character:")
if string[0]==prefix:
    if string[length-1]==suffix:
        print("Given string starts with a given prefix and ends with a given suffix") 
    else:
        print("Given string starts with a given prefix but not ends with given suffix") 

elif string[length-1]==suffix:
    print("Given string ends with a given suffix but not starts with given prefix") 
    
else:
    print("Given string is neither starts with given prefix nor ends with given suffix ")       