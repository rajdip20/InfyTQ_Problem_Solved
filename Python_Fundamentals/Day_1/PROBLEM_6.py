''' The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
        ● Rate per Adult: Rs. 37550.0
        ● Rate per Child: 1/3rd of the rate per adult
        ● Service Tax: 7% of the ticket amount (including all passengers)
        ● As it was a holiday season, the airline also offered a 10% discount on the final ticket
            cost (after inclusion of the service tax).
        ● Find and display the total ticket cost for a group which had adults and children. '''

rate = 37550.0
adults = int(input("Enter the number of adults: "))
children = int(input("Enter the number of children: "))
fare = adults * rate + children * (1/3) * rate
fare = fare + 0.07 * fare #service tax
fare = fare - 0.1 * fare
print("Total fare: ", round(fare, 2))
