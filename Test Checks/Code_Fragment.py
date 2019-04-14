# Comments have been removed for clarity of syntax

PI = 3.14159265

radius_str = input("Input the radius radius > 0)--> ")
radius_flt = float(radius_str)

circumference_flt = 2*PI*radius_flt

Area = PI*radius_flt*radius_flt

print("A circle with radius", radius_flt, \
      "has a circumference", circumference_flt,
      "and area", Area)
