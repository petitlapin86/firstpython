TICKET_PRICE = 10 #this is a constant

tickets_remaining = 100



#run this code continuously until we run out of tickets_remaining
while tickets_remaining >= 1:

    #output how many tickets are remaining using the tickets_remaining variable
    print("there are {} tickets remaining.".format(tickets_remaining))

    #gather the users name and assign it to a new variable
    name = input("What is your name: ")

    #prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}? ".format(name))

    #expect a value error to happen and handle it
    try:
        num_tickets = int(num_tickets) #reassign variable to number of tickets
        #make sure its a valid number of tix to request
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Uh Oh we ran into an issue. {}. Please try again".format(err))
    else:
        #calculate the price (number of tickets multiplied by the price) and assign it to a variable
        amount_due = num_tickets * TICKET_PRICE

        #output the total to the screen
        print("That will cost you {}".format(amount_due))

        #as a user i should be able to confirm my order Y/N?
        should_proceed = input("Would you like to purchase now? Type Y or N to proceed  ")
        if should_proceed.lower() == "y":
            print("SOLD!")
        #todo : gather credit card info and process it here.
            tickets_remaining -= num_tickets ##decrement tickets_remaining

        else: print("Thank you anyways, {} have a good day!".format(name))

#notify user that tickets are sold out
print("sorry the tickets are all sold out")
