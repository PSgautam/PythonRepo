#To print the sum of digits of a given number
def sum_of_digits(number):
    # Convert the number to its absolute value to handle negative numbers
    number = abs(number)
    
    sum_digits = 0
    
    # Calculate the sum of digits
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_digits += digit  # Add the digit to the sum
        number //= 10        # Remove the last digit
    
    return sum_digits

def main():
    number=int(input("Enter a number:"))
    
    try:
        result = sum_of_digits(number)
        print(f"The sum of the digits of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()





