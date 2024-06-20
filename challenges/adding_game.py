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


def main():
    #define return statements from functions
    difficulty = get_difficulty()
    number_of_questions = get_number_of_questions()
    questions_correct = 0
    
    #use for loop to ask amount of questions
    for questions in range(number_of_questions):
        #loop for difficulty
        #level 1 - 1 digit 0-9
        if difficulty == 1:
            level_1_value_1 = random.randint(0, 9)
            level_1_value_2 = random.randint(0, 9)
            level_1_sum = level_1_value_1 + level_1_value_2

            #set incorrect tries to 0
            incorrect_try = 0
            while True:
                try:
                    user_sum = int(input(f"\n{level_1_value_1} + {level_1_value_2} = "))
                    #if right, print correct
                    if user_sum == level_1_sum:
                        print("Correct!")
                        questions_correct = questions_correct + 1
                        break
                    if user_sum != level_1_sum:
                        #reprompt 2 times if question is wrong
                        print("Incorrect")
                        incorrect_try = incorrect_try + 1
                        #if wrong 3 times, print correct answer
                        if incorrect_try == 3:
                            print(f"The correct answer is {level_1_sum}")
                            break
                except:
                    print("Incorrect")
                    incorrect_try = incorrect_try + 1
                    if incorrect_try == 3:
                            print(f"The correct answer is {level_1_sum}")
                            break
                    
        #level 2 - 2 digits 10-99
        if difficulty == 2:
            level_2_value_1 = random.randint(10, 99)
            level_2_value_2 = random.randint(10, 99)
            level_2_sum = level_2_value_1 + level_2_value_2
            
            #set incorrect tries to 0
            incorrect_try = 0
            while True:
                try:
                    user_sum = int(input(f"\n{level_2_value_1} + {level_2_value_2} = "))
                    #if right, print correct
                    if user_sum == level_2_sum:
                        print("Correct!")
                        questions_correct = questions_correct + 1
                        break
                    if user_sum != level_2_sum:
                        #reprompt 2 times if question is wrong
                        print("Incorrect")
                        incorrect_try = incorrect_try + 1
                        #if wrong 3 times, print correct answer
                        if incorrect_try == 3:
                            print(f"The correct answer is {level_2_sum}")
                            break
                except:
                    print("Incorrect")
                    incorrect_try = incorrect_try + 1
                    if incorrect_try == 3:
                        print(f"The correct answer is {level_2_sum}")
                        break

        #level 3 - 3 digits 100-999
        if difficulty == 3:
            level_3_value_1 = random.randint(100, 999)
            level_3_value_2 = random.randint(100, 999)
            level_3_sum = level_3_value_1 + level_3_value_2

            #set incorrect tries to 0
            incorrect_try = 0
            while True:
                try:
                    user_sum = int(input(f"\n{level_3_value_1} + {level_3_value_2} = "))
                    #if right, print correct
                    if user_sum == level_3_sum:
                        print("Correct!")
                        questions_correct = questions_correct + 1
                        break
                    if user_sum != level_3_sum:
                        #reprompt 2 times if question is wrong
                        print("Incorrect")
                        incorrect_try = incorrect_try + 1
                        #if wrong 3 times, print correct answer
                        if incorrect_try == 3:
                            print(f"The correct answer is {level_3_sum}")
                            break
                except:
                    print("Incorrect")
                    incorrect_try = incorrect_try + 1
                    if incorrect_try == 3:
                        print(f"The correct answer is {level_3_sum}")
                        break
    
    #keep track and calculate percentage of correct answers
    percentage = questions_correct / number_of_questions * 100
    print(f"\nYou got {questions_correct} out of {number_of_questions} correct: {percentage:.2f}%")

main()
