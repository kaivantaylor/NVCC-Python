# PURPOSE: Create a non-scientific quiz for computer
# science aptitude.
# Kaivan Taylor
# CSC 200 - Introduction to Computer Science
# 10/15/17


import time # imports time functionalties into Python.

def ask_questions():
  
    total_score = 0

    # First question
    answer = input("Is your age over 45? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 1

    # Second question
    answer = input("Are you overweight? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 2
        
    # Third question
    answer = input("Do you smoke cigarettes on a regular basis? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 3

    # Fourth question
    answer = input("Do you exercise regularly? (y, Y, n, N) ")

    if answer in 'yY':
        total_score -= 2
    else:
        total_score += 2

    # Fifth question
    answer = input("Is your diet low in trans fat? (y, Y, n, N) ")

    if answer in 'yY':
        total_score -= 1
    else:
        total_score += 1

    # Sixth question
    answer = input("Do you consume vegetables on a regular basis? (y, Y, n, N) ")

    if answer in 'yY':
        total_score -= 1
    else:
        total_score += 1

    return total_score


# ================================== QUESTIONS==========================================

def aptitude(total_score_user):

    # From the total score, make a judgement about the aptitude.

    if -4 <= total_score_user <= -2:
        print("Very Low Aptitude")
    elif -1 <= total_score_user <= 1:
        print("Low Aptitude")
    elif 2 <= total_score_user <= 4:
        print("Average Aptitude")
    elif 5 <= total_score_user <= 7:
        print("High Aptitude")
    else: 
        print("Very High Aptitude")

    return

# ===================================== MAIN PROGRAM =====================================
while True:
    # Run main test
    print("\nHeart Attack Aptitude Test")
    total_score_user = ask_questions()
    aptitude(total_score_user)

    while True:
        # Ask user if they want to repeat the test
        answer = input("\nRun again? (y/n): ")
        if answer in ('y', 'n'):
            break
        else:
            print("Invalid input.")
    if answer == 'y':
        continue
    else:
        print("\nGoodbye!")
        time.sleep(2.0)
        break
        

        
        

        
            



