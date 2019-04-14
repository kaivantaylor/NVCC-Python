# PURPOSE: Write a program that prompts for a sentence and calculates
# the number of uppercase letters, lowercase letters, digits, and
# punctuation. Output the results neatly formatted and labeled in
# columns.
# Name: Kaivan Taylor
# Class: Computer Science I
# Professor: Timothy Seaman

import string

# ============================================================================#
def sentence_quantity_type():
    ask_user = input("Enter a sentence please! : ")

    uppercase_count = 0 # Count Variables for each type
    lowercase_count = 0
    digits_count = 0
    punctuation_count = 0

    for char in ask_user: # Add 1 to its respect count variable if matching
        if char in string.ascii_uppercase: 
            uppercase_count += 1
        elif char in string.ascii_lowercase:
            lowercase_count += 1
        elif char in string.digits:
            digits_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        else:
            pass

    lbl_1 = "Uppercase" # Labels for neatness
    lbl_2 = "Lowercase"
    lbl_3 = "Digit(s)"
    lbl_4 = "Punctuation"

    cnt_1 = str(uppercase_count) # Change integers to string for formatting
    cnt_2 = str(lowercase_count)
    cnt_3 = str(digits_count)
    cnt_4 = str(punctuation_count)

    print("\nQuantitative Results by Character")  # Header
    print("-"*52)

    print("{:13s}{:13s}{:13s}{:13s}".format(lbl_1,lbl_2,lbl_3,lbl_4))
    print("{:13s}{:13s}{:13s}{:13s}".format(cnt_1,cnt_2,cnt_3,cnt_4))

    print("-"*52)  
# ================================ M A I N ==================================#
sentence_quantity_type()

repeat = 1 # Value of 1 represents True, 0 is false

while repeat:
    ask_user = input("\nDo you want to run again? (y/n): ")
    if ask_user == 'y':
        print("\n")
        sentence_quantity_type()
    elif ask_user == 'n':
        repeat = 0
        print("Goodbye!")
    else:
        print("\nInvalid input!")
# ===========================================================================#
