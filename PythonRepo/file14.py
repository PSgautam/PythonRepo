#To read multiple lines entered by user until they enter an empty line and then print them.
def read_and_print_lines():
    lines = []
    print("Enter multiple lines of text :")
    
    while True:
        line = input("Enter the line:")
        if line == "":
            break
        lines.append(line)
    
    print("You entered:")
    for line in lines:
        print(line)   

# Run the function
read_and_print_lines()

