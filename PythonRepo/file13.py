#input the birth year
from datetime import date
birth_year=int(input("Enter the year:"))
today=date.today()    #today=2024-06-18
current_year=today.year  #current_year=2024

try:
    age=current_year-birth_year    #calculated age
    if age<0:
        print("Please enter a valid birth year.")
    else:
        print("you are",age,"years old")    #print the age of user
except ValueError:
    print("Enter a valid year like 1990")    
