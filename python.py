TICKET_PRICE = 10

tickets_remaining = 100

#output how many tickets are remaining using the tickets_remaining variable
print("there are {} tickets remaining.".format(tickets_remaining))

#gather the users name and assign it to a new variable
name = input("whats your name? ")

#prompt the user by name and ask how many tickets they would like
number_of_tickets = ("hey, {} how many tickets would you like? ".format(name))

number_of_tickets = int(number_of_tickets) #reassign variable to number of tickets

#calculate the price (number of tickets multiplied by the price) and assign it to a variable
amount_due = number_of_tickets * TICKET_PRICE

#output the total
print("the total due is ${}".format(amount_due))
