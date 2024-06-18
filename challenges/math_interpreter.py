def main():
    #must be X y Z
    #get X, y, and Z by splitting and looking for a space .split(" ")
    #check length of returned list. if not 3, input was in wrong format
    #if statement to check operator
    #output answer to expression
    while True:
        try:
            user_input = input("Expression: ")
            user_data = user_input.split(" ")
        except:
            continue


main()