"""Purpose: develop an algorithm to have the user
enter a polynomial and convert it into a list of
terms each of which has a coefficient and a power
of the variable."""
# Date: 11/15/17; in-class exercise
# Date: 11/27/17; revisions in-class exercise.

print("Enter a polynomial in the form: 3x^3 + 4x^2 - 5x + 2")
#poly_str = input("--> ")

poly_str = "4x^3 + x^2 - 5x + 7" # test polynomial
print(poly_str)
# the numbers at the end of statements correspond to steps on whiteboard
if poly_str[0] == "x":
    poly_str = "1" + poly_str

plus_sign_poly_str = poly_str.replace("-", "+-")   # 1
print(plus_sign_poly_str)
no_space_poly_str = plus_sign_poly_str.replace(" ", "") # 2
print( no_space_poly_str )
no_space_no_carat_poly_str = no_space_poly_str.replace("^", "") #3
print(no_space_no_carat_poly_str)
poly_with_1_coeffs_str = no_space_no_carat_poly_str.replace("+x", "+1x") #4
poly_with_1_coeffs_str = poly_with_1_coeffs_str.replace("-x", "-1x") #5
print(poly_with_1_coeffs_str)
poly_with_coeffs_and_degrees = poly_with_1_coeffs_str.replace("x+", "x1+") #6
print(poly_with_coeffs_and_degrees)

term_str_list = poly_with_coeffs_and_degrees.split("+") #7
print(term_str_list)

# search for constant term in list & make it look like the rest
coeff_deg_term_str_list = []
for term in term_str_list:
    if "x" in term:
        coeff_deg_term_str_list.append(term)
    else:
        coeff_deg_term_str_list.append(term + "x0")
print(coeff_deg_term_str_list)

# create an empty list for all of the terms of the polynomial
poly_terms_list = []
for term_str in coeff_deg_term_str_list:
    term_list = term_str.split("x")
    #print(term_list)
    coeff  = float(term_list[0])
    degree = int(term_list[1])
    #print(coeff, degree)
    term_list = [coeff, degree]
    print(term_list)
    poly_terms_list.append( term_list )
print(poly_terms_list)

# evaluate the poly for a given value
import decimal
y = 0

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)

x = 2 # evaluate th epoly for this value
y = 0 # accumulate the function value in y
for term in poly_terms_list:
    y = y + term[0]*x**term[1]
    y_float = float(y)
print("y = ", y_float)
    




    
