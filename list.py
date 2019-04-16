#Grocery List

#this is a list: language = ["python", "Javascript", "PHP", "Ruby"]
#lists are mutable

#.extend adds a list on to a list
#.append adds a list item
#del remove a list item - its really just deleting the label not the object
#.pop removes the last item of the list
#.copy makes a copy of the list
#.slice
#.split Split will take a string and create elements based on a delimiter
#.join takes an iterable and turns it into a string
#indexing list items starts at zero

def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help
    """)

show_help()

 while True: #infinite loop
     new_item = input("> ")

     if new_item == 'DONE':
         break #break out of loop with input done
     elif new_item == 'HELP':
         show_help()
