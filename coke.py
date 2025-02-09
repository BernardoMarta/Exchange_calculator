amount_due = input('Insert the price of the product:')
print(f'Amount Due: {amount_due}')
while amount_due > 0:
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in [25, 10, 5]:
        amount_due -= inserted_coin
    if amount_due <= 0:
        print(f'Change Owed: {-1 * amount_due}')
        break
    else:
        print(f'Amount Due: {amount_due}')
