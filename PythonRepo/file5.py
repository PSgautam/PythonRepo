#Input a string and write it to a text file.
s=input("Enter a string:")
with open("demo.txt","w") as demo:
    demo.write(s)
   