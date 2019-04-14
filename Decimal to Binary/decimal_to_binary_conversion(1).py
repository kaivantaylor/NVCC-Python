# Purpose: read a file of decimal numbers, convert each to a
# 32-bit binary number and output the 32-bit binary to a file.
# Author: in-class exercise. Date:10/25/17


def decimal_to_32_bit_binary(decimal_number, out_file):
    remainder_list = []

    while decimal_number > 0:
        quotient  = decimal_number // 2    
        remainder = decimal_number % 2
        remainder_list.append(  remainder  )
        decimal_number = quotient

    while len(remainder_list) < 32:
        remainder_list.append( 0 )

    remainder_list.reverse()

    for digit in remainder_list:
        print( digit, end = "", file = out_file )
    print( file = out_file )
# ------------------ main starts here ----------

my_input_file = open("decimal_data.txt", "r")
my_output_file= open("binary_data.txt",  "w")

for line_str in my_input_file:
    line_str = line_str.strip()
    line_int = int(line_str)
    decimal_to_32_bit_binary(line_int, my_output_file)

my_input_file.close()
my_output_file.close()
    



    
