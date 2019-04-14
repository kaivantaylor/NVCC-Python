# Test program for homework in CSC 200
# Kai
# 10/10/17

import time
import math

while True:
    p = input("Enter P: ")
    q = input("Enter Q: ")

    p = int(p)
    q = int(q)

    result = p > 0 and q < 0
    print(result)

    # Use a loop in order to ask user if the program wants to be re-run from the beginning    
    while True:
        answer = input('\nRun again? (y/n): ')
        if answer in ('y', 'n'): # If input by user is not 'y', or 'n' the loop will reiterate the "Run Again" string.
            break
        print( 'Invalid input.')
    if answer == 'y':
        continue
    else:
        print("\n")
        print("Goodbye!")
        time.sleep(2.0) # After inputting "n," the timer will count for two seconds before exiting the program.
        break



