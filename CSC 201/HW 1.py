# Name: Kaivan Taylor
# Assignment: Pg. 78 33,34,40, or 42
# CSC 201 - Computer Science I
# Calculate the simple interest by asking user for principal, rate, and time

print("Welcome to the Simple Interest Calculator!")

str_principal = input("Please enter the principal(dollars):")
str_rate = input("Please enter the rate of interest(percentage):")
str_time = input("Please enter the time(years):")

int_principal = int(str_principal)
float_rate = float(str_rate)
int_time = int(str_time)

format_percentage = float_rate/100

product_of_all = format_percentage*int_principal*int_time

final = product_of_all/100

print("Your simple interest is:",final)


