# Purpose: Create a non-scientific quiz for computer
# science aptitude. In-class exercise, 10/11/17

def ask_questions_get_total():
    """ Ask the user questions, total up response values and return
    the total to the calling program environment."""
    total_score = 0

    # first question:
    answer = input("Do you like to solve puzzles/problems? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score + 3
    else:
        total_score = total_score - 3

    # 2nd question:
    answer = input("Do you like to solve puzzles/problems? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score + 1

    # 3rd question:
    answer = input("Are you creative? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score + 2

    # 4th question:
    answer = input("Can you handle abstraction? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score + 1
    else:
        total_score = total_score - 1

    # 5th question:
    answer = input("Do you hate making mistakes? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score - 2

    # 6th question:
    answer = input("Do you like to learn new things? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score + 1
    else:
        total_score = total_score - 1

    # 7th question:
    answer = input("Do you understand the concept of 'grammar'? (y, Y, n, N) ")
    if answer in 'yY':
        total_score = total_score + 1
    else:
        total_score = total_score - 1

    return total_score
# ------------------------------------------------------------
def judge_aptitude(total_from_user):
    """From the total score, make a judgement about the aptitude"""
    if -8 <= total_from_user <= -6:
        print("very low aptitude")
    elif -5 <= total_from_user <= -3 :
        print("low aptitude")
    elif -2 <= total_from_user <= 3 :
        print("average aptitude")
    elif 4 <= total_from_user <= 6 :
        print("high aptitude")
    else:
        print("very high aptitude")
    return


# =================================== main program starts here ===========
# set up a loop for user repetition
do_again = True

while do_again:
    print("Non-Scientific Computer Aptitude Test")
    
    total_from_user = ask_questions_get_total()
    judge_aptitude(total_from_user)
    
    answer = input("Again? (y, Y, n, N) ")
    if answer in "nN" :
        do_again = False

               
