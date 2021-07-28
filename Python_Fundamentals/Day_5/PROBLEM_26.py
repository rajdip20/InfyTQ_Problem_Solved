''' A vendor at a food court is in the process of automating his order management system.
    The vendor serves the following menu – Veg Roll, Noodles, Fried Rice and Soup and also
    maintains the quantity available for each item. The customer can order any combination of
    items. The customer is provided the item if the requested quantity of item is available with the
    vendor.

    Write a python program which implements the following functions.
    place_order(*item_tuple): This function accepts the order placed by the customer. Consider it
    to be a variable length argument as each customer may have a different order.
    The function should check whether the items requested are present in the vendor’s menu and if
    so, it should check whether the requested quantity is available for each by invoking the
    check_quantity_available() method.
    
    The function should display appropriate messages for each item in the order for the below
    scenarios:
        1. When the requested item is not available in vendor’s menu, display <Item Name> is not
        available
        2. When the quantity requested by the customer is not available, display <Item Name>
        stock is over
        3. When the requested quantity of the item is available with the vendor, display <Item
        Name> is available
        
    check_quantity_available(index,quantity_requested): This function should check whether the
    requested quantity of the specified item is available. If so, it should reduce the quantity
    requested from the quantity available for that item and return True. Otherwise, it should return
    False.
    
    Test your code by using the given sample inputs.
    Verify your code by using the 2nd sample input(highlighted) given below:

                    Sample Input                               |    Expected Output   |
___________________________________________|___________________|______________________|
    Menu and quantity available            |    Items Ordered  |                      |
___________________________________________|___________________|______________________|
    (Veg Roll, Noodles, Fried Rice , Soup) |    Veg Roll,2     |Veg Roll is available |
    [2,200,250,3]                          |    Noodles,2      |Noodles is available  |
___________________________________________|___________________|______________________|
    (Veg Roll, Noodles, Fried Rice , Soup) |    Fried Rice,2   |                      |
    [2,200,3,0]                            |    Soup,1         |                      |
___________________________________________|___________________|______________________|

'''

menu = ('Veg Roll', 'Noodles', 'Fried Rice', 'Soup')
quantity_available = [2, 200, 3, 0]

def place_order(*item_tuple):
    item_tuple = list(item_tuple)

    while len(item_tuple) != 0:
        index = 0
        available = False
        for item in menu:
            if item == item_tuple[0]:
                available = check_quantity_available(index, item_tuple[1])
                if available == True:
                    print("{} is available".format(item_tuple[0]))
                else:
                    print("{} stock is over".format(item_tuple[0]))
                break
            index += 1
        if len(menu) == index:
            print("{} is not available".format(item_tuple[0]))
        del item_tuple[:2]


def check_quantity_available(index, quantity_requested):
    if quantity_available[index] >= quantity_requested:
        quantity_available[index] = quantity_available[index] - \
            quantity_requested
        return True
    else:
        return False


place_order("Fried Rice", 2, "Soup", 1)
