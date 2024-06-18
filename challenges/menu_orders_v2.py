#function to load menu items from the file and create a dictionary
#input: none
#output: dictionary of menu items
def get_menu_items():
    #create a file handle that gives access to the file. r to read, w to write
    data_file = open("menu.txt", "r")
    #create an empty dictionary to store menu items and prices
    menu_items = {}
    #loop through data in the file and read the file one line at a time
    for line_of_data in data_file:
        #split the line of data at the comma using .split()
        keys_and_values = line_of_data.split(",")
        #get item and price from the resulting list and create and store in the dictionary
        item = keys_and_values[0]
        price = float(keys_and_values[1])
        menu_items[item] = price
    #close the file
    data_file.close()
    return menu_items


def main():
    #load the menu items dictionary
    menu_items = get_menu_items()

    #while true, try to get input
    total = 0
    while True:
        try:
            user_item = input("\nItem: ")
            #if in dictionary, print price. else, reprompt user
            if user_item in menu_items:
            #add prices together and update total
                total = (menu_items[user_item]) + total
                print(f"Total: ${total:.2f}")
                continue
            #when user types "end" in any case, program ends
            if user_item.lower() == "end":
                break
            else:
                continue
        except:
            continue
    

main()