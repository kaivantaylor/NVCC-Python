# PURPOSE: Create a non-scientific quiz fr computer
# science aptitude. In-class exercise, 10/11/17
    
def ask_questions_get_total():
    # Ask the user questoins, total up response values and return
    # the total to the calling program environment.

    total_score = 0

    # First question
    answer = input("Do you like to solve puzzles/problems? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 3
    else:
        total_score -= 3

    # Second question
    answer = input("Do you like to work with computers? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 1
        
    # Third question
    answer = input("Are you creative? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 2

    # Fourth question
    answer = input("Can you handle abstraction? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 1
    else:
        total_score -= 1

    # Fifth question
    answer = input("Do you hate making mistakes? (y, Y, n, N) ")

    if answer in 'yY':
        total_score -= 2

    # Sixth question
    answer = input("Do you like to learn new things?? (y, Y, n, N) ")

    if answer in 'yY':
        total_score += 1
    else:
        total_score -= 1

    # Seventh question
    answer = input('Do you understand the concept of "grammar"? (y, Y, n, N) ')

    if answer in 'yY':
        total_score += 1
    else:
        total_score -= 1

    return total_score


# ======================================== MAIN PROGRAM ==================================================

def judge_student():

    # From the total score, make a judgement about the aptitude.

    if -8 <= total_from_user <= -6:
        print("Very Low Aptitude")
    elif -5 <= total_from_user <= -3:
        print("Low Aptitude")
    elif -2 <= total_from_user <= 3:
        print("Average Aptitude")
    elif 4 <= total_from_user <= 6:
        print("High Aptitude")
    else: 
        print("Very High Aptitude")
        
    return

#======================================= JUDGE APTITUDE =============================


total_from_user = ask_questions_get_total()

print(total_from_user)
judge_student(total_from_user)





