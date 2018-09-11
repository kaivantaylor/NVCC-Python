# PURPOSE: Examine a string and determine whether it is a valid
# string. In the string only include "(" and ")" to simplify the
# solution.
# Name: Kaivan Taylor
# Class: CSC 200 - Introduction to Computer Science I
# Professor Seaman
# Date: 3/31/2018

def recursive_function(test_file):

    a = len(test_file) # Not a global variable, only accesible in recursive_function().
 
    if a % 2 == 0: # Even numbered strings can be True.
        count_1 = 0 # Counter for ")"
        count_2 = 0 # Counter for "("
        
        for text in test_file[0]:
    
            if text == ")": # The beginning must be "(".
                return False
            
        for text in test_file[a-1]:
            
            if text == '(': # The end must be ")".
                return False
            
        for text in test_file:
            
            if text == ")": # Provide count for ")".
                count_1 += 1
            elif text == "(":
                count_2 += 1 # Provide count for "(".
            else: # Subtract from count to trigger False when any other character is entered
                count_1 -= 1
                
        if count_1 == count_2: # The number of "(" must equal ")".
            return True
        
        else: # Even amount of strings, but uneven amount of "(", ")" is False.
            return False
            
        if a == 1: # Iterate through the length of the string.
            return False
        
    else:
        return False

#--------------------------------MAIN---------------------------------------#

test_1 = '()'
test_2 = '))()()()' # ) At the beginning
test_3 = '(())()()((' # ( At the end
test_4 = '()()55()' # Numbers in string
test_5 = '()!()()' # Other value in string other than "(", ")"
test_6 = '())' # Odd numbered string
test_7 = '((()))'

assert recursive_function(test_1) == True, "Error in function method"
assert recursive_function(test_2) == False, "Error in function method"
assert recursive_function(test_3) == False, "Error in function method"
assert recursive_function(test_4) == False, "Error in function method"
assert recursive_function(test_5) == False, "Error in function method"
assert recursive_function(test_6) == False, "Error in function method"
assert recursive_function(test_7) == True, "Error in function method"

while True:
    try:
        user_str = input("\nEnter a string with only '(', or ')': ")

        print("The string is",recursive_function(user_str))

        while True:
            answer = input('\nRun again? (y/n): ')
            if answer in ('y', 'n'): # If input by user is not 'y', or 'n' the loop will reiterate the "Run Again" string.
                break
            print( 'Invalid input.')
        if answer == 'y':
            continue
        else:
            print("\nProgram will exit")
            break
        
    except IndexError:
        print("Invalid string for input, try again!")
    

