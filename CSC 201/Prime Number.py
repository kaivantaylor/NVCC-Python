# PURPOSE: Find all the prime numbers between 1 and 4027.
# Print them in a table reading down. Numbers should be
# right-justified in their column. Print a second page with
# twin prime numbers. Finally, print the number of primes
# found and the number of twin primes found. Label all
# tables with titles.
# CSC 201 - Computer Science I
# Name: Kaivan Taylor
#-----------------------------------------------------------------
def sort_num_prime():
    '''Sorts the number of primes from 1 to 4027
    and puts it in a list.'''
    prime_num = []
    for i in range(1,4028): # Input values from 1-4027.
        a = 2 # Divisible by 2.
        while i > a:
            if i % a == 0 & a != i: # Check if not
                #divisible by itself.
                break
            a += 1 # Increase by 1 for denominator.
        else:
            if i == 1:
                pass
            else:
                prime_num.append(i)
    return prime_num
#-----------------------------------------------------------------
def sort_num_twin(prime_num):
    '''Sorts the list of primes and converts into a
    list of twin primes.'''
    try:
        i = 0 # Start searching at index 0.
        twin_num = []
        while True:
            a = prime_num[i] # First index.
            b = prime_num[i+1] # Next index from first.
            if (b-a) == 2:
                twin_num.append(a) # Add to list
            i += 1 # Increase index search by 1.
    except IndexError: # If index is not found end.
        pass
    return twin_num
#-----------------------------------------------------------------
def print_prime_num(prime_num):
    '''Prints out a list of primes using list from
    primes.'''
    print("Prime Numbers") # Title.
    print("="*20)    
    for num in prime_num: # Print prime numbers (Right-adjusted).
        print("{:>10d}".format(num))
    print("-"*20,"\n")
#-----------------------------------------------------------------
def print_twin_prime_num(prime_num):
    '''Prints out a list of twin primes using list from
    primes.'''
    print("Twin Prime Numbers") # Title.
    print("="*20)
    try:
        i = 0 #Start searching at index 0.
        while True:
            a = prime_num[i] # First index.
            b = prime_num[i+1] # Next index from first.
            if (b-a) == 2: # Print twin number (Right-adjusted).
                print("{:>10d}{:>10d}".format(a,b))
            i += 1 # Increase index search by 1
    except IndexError: # If index is not found, do nothing else.
        pass
    print("-"*20,"\n")
#-----------------------------------------------------------------
prime = sort_num_prime() # Assign variable for list of primes
twin_prime = sort_num_twin(prime) # Assign variable for list of twins.

print_prime_num(prime) # Print out primes.
print_twin_prime_num(prime) # Print out twin primes.

prime_length = len(prime) # Calculate length of prime list.
twin_length = len(twin_prime) # Calculate length of twin primes list.

print("There are",prime_length,"prime(s) found.")
print("There are",twin_length,"twin prime(s) found.")

Exit = input("Press enter to exit...") # For when opened in terminal.



