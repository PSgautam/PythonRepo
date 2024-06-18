#To copy the content of one file to another
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        with open(destination_file, 'w') as dst:
            dst.write(content)
        
        print(f"Contents of {source_file} have been successfully copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: {source_file} does not exist.")
    except IOError as e:
        print(f"Error: An I/O error occurred. {e}")

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
