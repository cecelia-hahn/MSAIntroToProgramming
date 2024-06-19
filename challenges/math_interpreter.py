def main():
    print("Type math expressions in terms of X y Z with y being the operator. Type 'end' to stop the program.\n")  
    while True:
        try:
            #must be X y Z
            user_input = input("\nExpression: ")
            #check if user wants to end program
            if user_input.lower() == "end":
                break
            #get X, y, and Z by splitting and looking for a space .split(" ")
            user_data = user_input.split(" ")
            #check length of returned list. if not 3, input was in wrong format
            if len(user_data) == 3:
                integer_1 = float(user_data[0])
                integer_2 = float(user_data[2])
                operator = user_data[1]
                #if statements to check operator
                if operator not in ["+", "-", "/", "*"]:
                    print("Invalid input. Please type in a valid operator.")
                if operator == "+":
                    #output answer to expression
                    sum = integer_1 + integer_2
                    print(f"{sum:.1f}")
                if operator == "-":
                    difference = integer_1 - integer_2
                    print(f"{difference:.1f}")
                if operator == "*":
                    product = integer_1 * integer_2
                    print(f"{product:.1f}")
                if operator == "/":
                    if integer_2 == 0:
                        print("You can't divide by zero")
                    else:
                        quotient = integer_1 / integer_2
                        print(f"{quotient:.1f}")
            else:
                print("Invalid input. Please type in X y Z format.")
        except:
            continue

main()

#to make code more concise, make one answer variable and print the answer at the very end
