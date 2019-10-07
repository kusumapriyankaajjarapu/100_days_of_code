"""
Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned
below:
The ticket number should be generated as airline:src:dest:number
where
*Consider AI as the value for airline
*src and dest should be the first three characters of the source and destination cities.
*number should be auto-generated starting from 101
The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket number
"""



def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    if(no_of_passengers < 5):
        i = 0
    else:
        i = no_of_passengers - 5
    while(i < no_of_passengers):
        number = 101 + i
        s = airline + ":"+source[0:3] + ":"+ destination[0:3] + ":"+ str(number)
        ticket_number_list.append(s)
        i +=1 
    return ticket_number_list


print(generate_ticket("AI","Bangalore","London",7))
