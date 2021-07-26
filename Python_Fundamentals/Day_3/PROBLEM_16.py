''' Write a python program to generate the ticket numbers for specified number of passengers
    traveling in a flight as per the details mentioned below:
    The ticket number should be generated as airline:src:dest:number

    where
        1. Consider AI as the value for airline
        2. src and dest should be the first three characters of the source and destination cities.
        3. number should be auto-generated starting from 101

    The program should return the list of ticket numbers of last five passengers.
    Note: If passenger count is less than 5, return the list of all generated ticket numbers.

     |  Sample Input       |                         Expected Output                                          |
     |_____________________|__________________________________________________________________________________|
     |  airline = AI       |        ['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108', 'AI:Ban:Lon:109',  |
     |                     |        'AI:Ban:Lon:110']                                                         |
     |  source =           |                                                                                  |
     |  Bangalore          |                                                                                  |
     |                     |                                                                                  |
     |  destination =      |                                                                                  |
     |  London             |                                                                                  |
     |                     |                                                                                  |
     |  no_of_passengers   |                                                                                  |
     |  = 10               |                                                                                  |
     |_____________________|__________________________________________________________________________________|
     |  airline = BA       |        ['BA:Aus:Fra:101', 'BA:Aus:Fra:102']                                      |
     |                     |                                                                                  |
     |  source = Australia |                                                                                  |
     |                     |                                                                                  |
     |  destination =      |                                                                                  |
     |  France             |                                                                                  |
     |                     |                                                                                  |
     |  no_of_passengers   |                                                                                  |
     |  = 2                |                                                                                  |
     |_____________________|__________________________________________________________________________________|

'''

def get_tickets(ai, src, dest, no):
    t_no = 101
    ai = ai.upper()
    src = src[:3]
    dest = dest[:3]
    l = []
    for i in range(no):
        s = ai + ":" + src + ":" + dest + ":" + str(t_no)
        l.append(s)
        t_no += 1
    l = l[-5:]
    return l

airline = input("Enter your airline:[2 characters] ")
source = input("Enter your source city: ")
destination = input("Enter your destination city: ")
number = int(input("Enter the number of passengers: "))
print(get_tickets(airline, source, destination, number))
