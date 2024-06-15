#create a program that accepts a hwy number and output the direction
#user enters: 95
#output: "Interstate 95 runs South to North"
#error check program so that it doesn't crash

#get hwy number from user
def get_hwy_number():
    while True:
        try:
            hwy_number = int(input("\nEnter a highway number: "))
            if (hwy_number <= 0):
                print("ERROR: Please enter a number higher than 0")
                continue
            else:
                break
        except:
            print("ERROR: Enter a number higher than 0")
    return hwy_number

#calculate direction
def calculate_direction(hwy_number):
    if (hwy_number % 2 == 0):
        return "East to West"
    else:
        return "North to South"
#or you could write a function for "check even" and return either true or false, then create another if statement called if hwy_number_even and print their respective statements (in main function)

def main():
    while True:
        #print output
        hwy_number = get_hwy_number()
        direction = calculate_direction(hwy_number)
        print(f"Interstate {hwy_number} runs {direction}.")
        
        #ask user if they want to run the program again
        run_again = input("\nWould you like to run the program again? Enter 'y' to continue: ")
        if (run_again == "y"):
            continue
        else:
            break

main()