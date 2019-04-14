# Purpose: Develop an algorithm to have the user
# enter a polynomial and convert it into a list of
# terms each of which has a coefficient and a power
# of the variable.
# Name: Kaivan Taylor
# Date: 11/28/17

import decimal

# Step 1 - Ask user to input a polynomial

print("Enter a polynomial in the form: 3x^3 + 4x^2 - 5x + 2")
poly_str = input("--> ")
#poly_str = "4x^3 + x^2 - 5x + 7" # Test polynomial
print(poly_str) # Print out the input of the polynomial

if poly_str[0] == "x": # Set non-existant 1 to only inputs of "x".
    poly_str = "1" + poly_str

plus_sign_poly_str = poly_str.replace("-", "+-")   # 1 Replace minus with equivalent of +-
#print(plus_sign_poly_str)
no_space_poly_str = plus_sign_poly_str.replace(" ", "") # 2 Remove spaces
#print( no_space_poly_str )
no_space_no_carat_poly_str = no_space_poly_str.replace("^", "") # 3 Remove unnecessary carrots
#print(no_space_no_carat_poly_str)
poly_with_1_coeffs_str = no_space_no_carat_poly_str.replace("+x", "+1x") # 4 Insert 1 for values with "x"
poly_with_1_coeffs_str = poly_with_1_coeffs_str.replace("-x", "-1x") # 5 Insert -1 for values with "-x"
#print(poly_with_1_coeffs_str)
poly_with_coeffs_and_degrees = poly_with_1_coeffs_str.replace("x+", "x1+") # 6 Insert 1 for polynomials with only one coefficient
#print(poly_with_coeffs_and_degrees)
term_str_list = poly_with_coeffs_and_degrees.split("+") # 7 Split the list between strings with "+"
#print(term_str_list)

# Search for constant term in list & make it look like the rest
coeff_deg_term_str_list = []
for term in term_str_list:
    if "x" in term:
        coeff_deg_term_str_list.append(term)
    else:
        coeff_deg_term_str_list.append(term + "x0")
print(coeff_deg_term_str_list)

# Create an empty list for all of the terms of the polynomial
poly_terms_list = []
for term_str in coeff_deg_term_str_list:
    term_list = term_str.split("x")
    #print(term_list)
    coeff  = float(term_list[0])
    degree = int(term_list[1])
    #print(coeff, degree)
    term_list = [coeff, degree]
    #print(term_list)
    poly_terms_list.append( term_list )
#print(poly_terms_list)

# evaluate the poly for a given value
user_input = input("Enter name of output file: ")
output = open(user_input+".txt","w")

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)
    
a_str = input("Where do I start from x? ")
b_str = input("Where do I end at x? ")
a = int(a_str)
b = int(b_str)

for x in drange(a,b+.1,0.2):
    y = 0
    for term in poly_terms_list:
        first = x**term[1]
        #print(first)
        second = term[0]
        #print(second)
        sum = first* second
        y += sum
    print("y=","{:.3f}".format(y),"at x=", x,file=output)

print("Done!")
output.close()
