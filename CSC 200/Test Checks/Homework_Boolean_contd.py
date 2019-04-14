# Program that uses loop to print a statement
# depending on what the variables equal.
# Kai
# 10/10/17

while True:
    
    x = input("Enter x: ")
    y = input("Enter y: ")
    a = input("Enter a: ")
    b = input("Enter b: ")

    x = float(x)
    y = float(y)
    a = float(a)
    b = float(b)

    if x < y:
        if x > b:
            print("America")
        else:
            print("Australia")
    else:
        if a > b:
            print("Europe")
        else:
            print("Asia")
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
