# PURPOSE: Demonstrate the use of a file.
# In-class exercise. Oct 18, 2017.

# Step 1 - Open the file
input_file = open("cars.txt", "r")

# Step 2 - Check that the file opened

# Step 3 - Use the data in the file
for line_str in input_file:
    line_str = line_str.strip()
    print(line_str)
    # line_number = int(line_str)
    # if line_number >= 500:
    #    print(line_number)

# Step 4 - Close the file
input_file.close()
