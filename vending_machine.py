#write function to see if coins in accepted value
#return true or false
#if true, subtract from amount due
#if amount due is < 0, show owed change


def main():
    amount_due = 50
    print("Vending Machine\n---------------")
    while True:
        print(f"\nAmount Due: {amount_due}")
        try:
            user_coins = int(input("Insert Coin: "))
            if user_coins in [1, 5, 10, 25]:
                amount_due = amount_due - user_coins
                if amount_due > 0:
                    continue
                else: 
                    change_owed = abs(amount_due)
                    print(f"\nChange owed: {change_owed}")
                    break
            else:
                continue
        except:
            continue
    

main()