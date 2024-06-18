#Read from CSV file and print its content on console
import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(row)  # Print each row as a comma-separated string
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: An error occurred while reading the file. {e}")

def main():
    filename = input("Enter the CSV file name: ")
    read_csv_file(filename)

if __name__ == "__main__":
    main()

    