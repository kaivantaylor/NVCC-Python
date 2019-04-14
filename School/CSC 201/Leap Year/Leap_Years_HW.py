1# Purpose: Write a program to read in a file of years
# (1583 <= year <= 10,000), one per line, and output to
# a serparate file with only those years that are leap
# years.
#   ** Ask user to input file names of both files and
# use try-except when opening each file. Must have at
# least two functions
# Name: Kaivan Taylor
# CSC 201 - Computer Science I - Professor Seaman

#-----------------------------------------------------------------------------#
def ask_input_file_name():
    '''Asks user for a file to open. If not found, asks question again.'''
    
    ask_user_file_name = input("What is the name of the input file?: ")
    while True:   
        try:
            user_file = open(ask_user_file_name + ".txt", "r")
            break
        except IOError: # If the file is not found, ask user to re-enter name.
            ask_user_file_name = input("\nFile not found, please try again: ")
    return user_file

#------------------------------------------------------------------------------#
def ask_output_file_name():
    '''Asks user for name of the output file.'''
    
    ask_user_file_name = input("\nWhat is the name of the output file?: ")
    while True:   
        try:
            user_file = open(ask_user_file_name + ".txt", "w")
            break
        except IOError: # If input contains invalid characters, re-enter name.
            ask_user_file_name = input("\nInvalid file name, please try again: ")
    return user_file

#------------------------------------------------------------------------------#
def filter_input_file(user_input_file,user_output_file):
    '''Filters out numbers by:
    1) Striping white space
    2) Restricting the length of all characters to four,
    3) Converting the numbers to integers if possible,
    4) Sorting numbers only valid in the Gregorian Calendar
    5) Calculating the years using a formula to determine if it is a leap year'''

    four_len_list = [] # Create lists to hold values from the user input file.
    number_list = []
    year_list = []

    for line_str in user_input_file:
        line_str = line_str.strip() # Remove whitespace.
        four_len_str = line_str[:4] # Restrict length to 4.
        four_len_list.append(four_len_str)
    print(four_len_list)
          
    for char in four_len_list:
        try:
            filtered_numbers_str = int(char) # Removes characters, floats, and
            # other value types except integers using try-except statement.
            number_list.append(filtered_numbers_str)
        except ValueError:
            pass

    for numbers in number_list: # Sorts year according to the Gregorian Calendar.
        if 1583 <= numbers <= 10000:
            year_list.append(numbers)
          
    for year in year_list: # Leap year can be divisible by 4 and not 100. It is
        # also a leap year if divisible by 400.
        if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
            print(year, file = user_output_file)
            
#---------------------------------M A I N---------------------------------------#
#user_input_file = ask_input_file_name() # Assign variables for file names
user_input_file = open("all_years.txt","r")
user_output_file = ask_output_file_name()

filter_input_file(user_input_file,user_output_file) # Call "filtering" function
# with file name variables

user_input_file.close()
user_output_file.close() # Close both input and output files

