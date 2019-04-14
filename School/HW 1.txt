# Name: Kaivan Taylor
# Assignment: Pg. 78 33,34,40, or 42
# CSC 201 - Computer Science I
# Calculate the simple interest by asking user for principal, rate, and time

print("Welcome to the Simple Interest Calculator!")

str_principal = input("Please enter the principal(dollars):") # Ask user to give a value for principal, rate, and time.
str_rate = input("Please enter the rate of interest(percentage):")
str_time = input("Please enter the time(years):")

int_principal = int(str_principal) # Format values to integer and float values accordingly.
float_rate = float(str_rate)
int_time = int(str_time)

format_percentage = float_rate/100 # Change percentage into decimal form

product_of_all = format_percentage*int_principal*int_time # Find the product of principal, rate, and time.

final = product_of_all/100 # Divide the final sum by 100 for the final answer.

print("Your simple interest is:",final) # Print out answer to user. 


