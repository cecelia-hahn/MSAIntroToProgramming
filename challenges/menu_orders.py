def main():
    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

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
