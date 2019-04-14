# PURPOSE: Turn a demical into binary from a .txt file and output into
# a new .txt file.
# Kaivan Taylor
# CSC 200 Homework
# 10/31/17

def converter_method(decimal, output_file): # Define the conversion method
    remainder_vector = [] # Create array for storing data        

    while decimal > 0:   # Run loop until division by 2 cannot be done (quotient is 0)
        quotient = decimal // 2
        remainder = decimal % 2    # Find whether remainder is 0 or 1
        remainder_vector.append(remainder) # Add remainder to array
        decimal = quotient
    while len(remainder_vector) < 32: # Format conversion to a 32-bit length
        remainder_vector.append(0)

    remainder_vector.reverse() # Reverse order of array to imitate steps taken when solving by hand

    for digit in remainder_vector:  # Print the final converted form to an output file ".txt"
        print(digit, end = "", file = output_file)
    print(file = output_file)

# -------------------------conversion method-----------------------#

ask_user_input = input("Enter the name of the input .txt file: ")
ask_user_output = input("Enter the name of the output .txt file: ")

user_input_file = open(ask_user_input, "r")  # Specify input file with "read" function
user_output_file = open(ask_user_output, "w") # Specify output file with "write" function

for line_str in user_input_file:    # Loop to format input file before passing to conversion method
    line_str = line_str.strip()
    line_int = int(line_str)
    converter_method(line_int, user_output_file)

user_input_file.close() # Close both files 
user_output_file.close()
