#To remove all punctuation from a string
str1=input("Enter  string:")
punctuation='''!()-[]{}:;'"\\,<>./?@#$%^&*_'''
cleaned_string=""
for char in str1:
    if char not in punctuation:
      cleaned_string+=char
print("String without punctuations:",cleaned_string) 


