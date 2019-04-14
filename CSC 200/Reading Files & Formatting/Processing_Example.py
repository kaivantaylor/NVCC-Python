input_file = open("numbers.txt", "r")
output_file = open("numbers_and_squares.txt","w")

for line_str in input_file:
    line_str = line_str.strip()
    num_float = float(line_str)
    square_flt = num_float*num_float
    print("{:5.1f} {:5.1f}".format(num_float,square_flt), file = output_file)

input_file.close()
output_file.close()
