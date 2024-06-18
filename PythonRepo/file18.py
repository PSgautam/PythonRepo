#To check if two strings are anagrams of each other.
str1=input("Eenter 1st string:")
str2=input("Enter 2nd string:")
str1.replace(" ","").lower()
str2.replace(" ","").lower()

if sorted(str1)==sorted(str2):
    print("Given 2 strings are anagrams of each other.")
else: 
    print("Given 2 strings are not anagrams of each other.")   

  