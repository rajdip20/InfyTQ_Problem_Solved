''' The road transport corporation (RTC) of a city wants to know whether a particular bus-route
    is running on profit or loss.

    Assume that the following information are given:
    Price per litre of fuel = 70
    Mileage of the bus in km/litre of fuel = 10
    Price(Rs) per ticket = 80
    
    The bus runs on multiple routes having different distance in kms and number of passengers.
    Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case
    of loss.
'''

def calculate_profit(distance, passengers):
    price_per_litre = 70
    mileage = 10
    price_per_ticket = 80
    fule_consumed = distance / mileage
    spent = fule_consumed * price_per_litre
    earned = passengers * price_per_ticket
    profit = earned - spent

    if profit < 0:
        return -1
    else:
        return profit

d = int(input("Enter the distance: "))
p = int(input("Enter the number of passengers: "))
print(calculate_profit(d, p))
