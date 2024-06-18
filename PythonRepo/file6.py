#Read the content of txt file and print it on console.
try:
    with open("demo.txt","r") as demo:
        content=demo.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print("File does not exist")
    
