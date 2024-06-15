#write function to see if coins in accepted value
#return true or false
#if true, subtract from amount due
#if amount due is < 0, show owed change

def main():
    amount_due = "50"
    print(f"Vending Machine\n---------------\nAmount Due: {amount_due}")
    while True:
        try:
            user_coins = int(input("Insert Coin: "))
            if user_coins in [1, 5, 10, 25]:
                print(f"Amount Due: {amount_due} - {user_coins}")
                break
            else:
                continue
        except:
            continue
    

main()