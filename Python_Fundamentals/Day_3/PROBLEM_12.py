''' ARS Gems Store sells different varieties of gems to its customers.

    Write a Python program to calculate the bill amount to be paid by a customer based on the list
    of gems and quantity purchased. Any purchase with a total bill amount above Rs.30000 is
    entitled to 5% discount. If any gem required by the customer is not available in the store, then
    consider total bill amount to be -1.

    Assume that quantity required by the customer for any gem will always be greater than 0.
    
    Perform case-sensitive comparison wherever applicable.

    gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
    
    #Price of gems available in the store. gems_list and price_list have one-to-one correspondence
    price_list=[1760,2119,1599,3920,3999]

    #List of gems required by the customer
    reqd_gems=["Ivory","Emerald","Garnet"]
    
    #Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one
    correspondence
    reqd_quantity=[3,10,12] 
'''

def calculate_bill_amount(reqd_gems, reqd_quantity):
    gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
    price_list = [1760, 2119, 1599, 3920, 3999]
    price = 0

    for i in range(len(reqd_gems)):
        gem = reqd_gems[i]
        if gem in gems_list:
            index = gems_list.index(gem)
            price = price + (price_list[index] * reqd_quantity[i])
        else:
            return -1
    
    if price > 30000:
        price = price - 0.05 * price
    return price


reqd_gems = ["Ivory", "Emerald", "Garnet"]
reqd_quantity = [3, 10, 12]
print(calculate_bill_amount(reqd_gems, reqd_quantity))
