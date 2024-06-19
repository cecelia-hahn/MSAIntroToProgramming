import random

#ask difficulty level 1, 2, or 3 as a function
def get_difficulty():
    while True:
        try:
            difficulty = int(input("\nEnter a difficulty level 1-3: "))
            if difficulty in [1, 2, 3]:
                break
            #prompt again if not valid
            else:
                print("Error: Type in a number 1-3")
                continue
        except:
            print("Error: Type in a number 1-3")
            continue
    return difficulty

#ask number of questions 3 - 10 as a function
def get_number_of_questions():
    while True:
        try:
            user_questions = int(input("\nEnter number of questions to ask 3-10: "))
            if user_questions >= 3 and user_questions <= 10:
                break
            #prompt again if not valid
            else:
                print("Error: Type in a number 3-10")
                continue
        except:
            print("Error: Type in a number 3-10")
            continue
    return user_questions

#reprompt 2 times if question is wrong
#if right, print correct
#if wrong 3 times, print correct answer

#keep track and calculate percentage of correct answers

def main():
    #define return statements from functions
    difficulty = get_difficulty()
    number_of_questions = get_number_of_questions()
    #loop for difficulty
    #level 1 - 1 digit 0-9
    #level 2 - 2 digits 10-99
    #level 3 - 3 digits 100-999

    #use for loop to ask amount of questions

main()