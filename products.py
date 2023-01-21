LAST_INDEX_RANGE = 0
PRODUCT_DB = [
    {"name": "Car", "price": 2.90},
    {"name": "Milk", "price": 1.90},
    {"name": "Bread", "price": 4.90},
    {"name": "Rice", "price": 0.90},
    {"name": "Carrot", "price": 2.90},
    {"name": "Milk-Candy", "price": 1.90},
    {"name": "Butter", "price": 4.90},
    {"name": "Rolex", "price": 0.90},
]


def display_products(product_list):
    global LAST_INDEX_RANGE

    new_index_pos = LAST_INDEX_RANGE + 3
    LAST_INDEX_RANGE = new_index_pos
    return product_list[LAST_INDEX_RANGE: new_index_pos]


def search_product(name):
    global PRODUCT_DB
    result = []
    for product in PRODUCT_DB:
        if product['name'] == name:
            result.append(product)
    return result


MENU = """1) View Next
2)View Prev 
3) Reset View
4) Search
>>>
"""

SEARCH_MENU = """What filter would you like to search for your item by. By:
1)Name 
2)Price"""


print("Hello Welcome to our store")
while True:
    choice = input(MENU)
    if choice == "1":
        display_products(PRODUCT_DB)
    elif choice == "4":
        while True:
            LAST_INDEX_RANGE = 0
            name = input(SEARCH_MENU)
            result = (search_product(name))
            if len(result) > 3:
                while True:
                    action = input("1) View next 2) View Previous 3) Exit search view")
                    if action == "1":
                        prod_display = display_products(result)
                        if len(prod_display) > 0:
                            print(prod_display)
                        else:
                            print("All products displayed. Resetting product view")
                            LAST_INDEX_RANGE = 0
                    elif action == "3":
                        print("Exiting search")
                        break
                
    else:
        break
    print()
