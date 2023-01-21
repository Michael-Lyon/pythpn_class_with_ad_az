import random

"""
A reservation system. 
This is to enable a user book a table at a resturant.

Types of table and prices
the number of avaiable tables
"""

SILVER_PRICE = 100_000
GOLD_PRICE = 200_000
PLATINUM_PRICE = 350_000

silver_table_available = 20
gold_table_available = 10
platinum_table_available = 5

def sell_table(table_id: int):
    global silver_table_available, account_balance
    print("How many tables would you like to reserve")
    table_num = int(input("> "))
    if silver_table_available > 0 and table_num <= silver_table_available:
        approve_payment = input("make payment?(y/n)> ")
        if approve_payment == "y":
            account_balance -= SILVER_PRICE
            if account_balance > 0:
                silver_table_available -= table_num
                print("Purchase completed")
            else:
                print("Insuffficient funds")
        else:
            print("How can we make our service better for you.")
    else:
        print("No table avaiable")

MENU = f"""Welcome to ADAZ Cuisine
Please kindly make your choice of tables:
    1) Silver Table:
        Price: {SILVER_PRICE}
        Available: {silver_table_available}
    2) Gold Table:
        Price: {GOLD_PRICE}
        Available: {gold_table_available}
    3) Platinum Table:
        Price: {PLATINUM_PRICE}
        Available: {platinum_table_available}
    enter table of choice here>
"""
choice = input(MENU)
account_balance = random.randint(100_000, 1_000_000)
if choice == '1':
    print("Table of choice selected")
    sell_table(1)
elif choice == '2':
    print("Great choice")
    sell_table(2)
elif choice == '3':
    print("Superb choice")
    sell_table(3)
else:
    print("Invalid choice")