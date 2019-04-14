"""Purpose: experimnet with lists and dictionaries.
Hands-on examples in class. Date: November 6, 2017."""

# ------------------- List example ----
#gro_list = ["eggs", "milk", "butter", "berries", "squash",\
#             "tacos", "beans", 'flour', "chocolate", 'tea', "coffee"]
#print( gro_list)
#counter = 0
#for item in gro_list:
#    counter += 1
#    print(  "{:2d}. {:s}".format(counter, item)  )

# -------------- obtain the list from a file --------
##gro_list = []   # set grocery list to null; read data from a file.
##gro_inv_file = open("grocery_inventory_file.txt", "r")
##
##for line in gro_inv_file:
##    line = line.strip()
##    gro_list.append(line)
### now print all grocery items in a master list
##counter = 0
##for item in gro_list:
##    counter += 1
##    print(  "{:2d}. {:s}".format(counter, item)  )
##gro_inv_file.close()
# ------------------- Introduction to dictionaries
##price_dictionary = {"eggs":1.90, "milk":2.95, "butter":4.25, "berries":3.99}
###print( price_dictionary )
##for key in price_dictionary:
##    print(key, price_dictionary[key] )
# read the dictionary from a file
grocery_dictionary = {}  # init to null/empty dictionary
gro_inventory_file = open("grocery_list_test.txt", "r")

for line in gro_inventory_file:
    line = line.strip()     # throw away newline character
    product_list = line.split()  # split into key & value in a list
    #print(product_list)
    #print( product_list[0], product_list[1] )
    key = product_list[0]
    value = float(product_list[1])
    grocery_dictionary[ key ] = value
#print( grocery_dictionary )
gro_inventory_file.close()

# ------------ make a grocery list of tuples --------
my_gro_list = [ (2, "eggs"),  (1, "butter"), (3, "bread"), (5, "apples") ]
total_cost = 0
for item in my_gro_list:
    #print( item )
    quantity = int( item[0] )
    editable_thing = item[1]
    print(editable_thing)
    unit_price = grocery_dictionary[ editable_thing ]
    extension = quantity*unit_price
    print( quantity, editable_thing, unit_price, extension)
    total_cost = total_cost + extension
print("Total of all itms: ", total_cost)
    
















