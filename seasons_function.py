#THIS DOES NOT WORK
def get_month():
    while True:
        try:
            month_number = int(input("Enter a number 1-12: "))
            if month_number < 1 or month_number > 12:
                print("ERROR: Enter a number between 1 and 12")
                continue
            else:
                break
        except: 
            print("ERROR: Enter a number between 1 and 12")
    return month_number

#create a function to return the season based on month
#input: month number
#output: season name
def get_season_number(month_number):
    if month_number in ["12", "1", "2"]:
        return "winter"
    elif month_number in ["3", "4", "5"]:
        return "spring"
    elif month_number in ["6", "7", "8"]:
        return "summer"
    elif month_number in ["9", "10", "11"]:
        return "fall"
    else:
        print("ERROR: Enter a number between 1-12")


def main():
    while True:
        month_number = get_month()
        season_name = get_season_number(month_number)
        print(f"The season is {season_name}")

        #ask user if they want to run the program again
        run_again = input("Do you want to run the program again? y or Y: ")
        if run_again == "y" or run_again == "Y":
            continue
        else:
            break
main()