def main():
#create a decision structure to determine the season based on the month
    #winter: 12, 1, 2; spring: 3, 4, 5; summer: 6, 7, 8; fall: 9, 10, 11
    #ask the user to enter the number of the month
    #output the season based on the number
    while True:
        try:
            input_month = int(input("Enter a month as a number between 1 and 12: "))
            if (input_month == 12 or input_month == 1 or input_month == 2):
                print("\nThe season is winter")
                break
            elif (input_month == 3 or input_month == 4 or input_month == 5):
                print("\nThe season is spring")
                break
            elif (input_month == 6 or input_month == 7 or input_month == 8):
                print("\nThe season is summer")
                break
            elif (input_month == 9 or input_month == 10 or input_month == 11):
                print("\nThe season is fall")
                break
            else:
                print("ERROR: Enter a number between 1 and 12")
        except:
            print("ERROR: Enter a whole number between 1 and 12")
            continue

    #or you could write a function to get the month number and return it, then go through if statements to print the month
    #def get_month_number():
    #while True:
    #try:
    #month_number = int(input("enter a number 1-12"))
    #if month_number < 1 or month_number > 12:
    #print("error message")
    #continue
    #else:
    #break
    #except: (write another error under)
    #return month_number
    #then write if and elif statements to print the month in words

    print("\n\n")

    #ORRRRRRR
    while True:
        month_number = input("Enter a month number 1-12: ")
        if month_number in ["12", "1", "2"]:
            print("It is winter")
        elif month_number in ["3", "4", "5"]:
            print("It is spring")
        elif month_number in ["6", "7", "8"]:
            print("It is summer")
        elif month_number in ["9", "10", "11"]:
            print("It is fall")
        else:
            print("ERROR: Enter a number between 1-12")
            continue
        break
    #can put break in between each or at the end in line with ifs
main()