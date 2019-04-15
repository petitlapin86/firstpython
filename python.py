TICKET_PRICE = 10

tickets_remaining = 100

#output how many tickets are remaining using the tickets_remaining variable
print("there are {} tickets remaining.".format(tickets_remaining))

#gather the users name and assign it to a new variable
name = input("What is your name: ")

#prompt the user by name and ask how many tickets they would like
num_tickets = input("How many tickets would you like, {}? ".format(name))

num_tickets = int(num_tickets) #reassign variable to number of tickets

#calculate the price (number of tickets multiplied by the price) and assign it to a variable
amount_due = num_tickets * TICKET_PRICE

#output the total
print("That will cost you {}".format(amount_due))
