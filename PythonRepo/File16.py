#To count the frequency of each character of a string
string=input("Enter a string:")
frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1 
    else:
        frequency[char]=1 
print(frequency) 
for key,value in frequency.items():

    print(f"{key} : {value}")         