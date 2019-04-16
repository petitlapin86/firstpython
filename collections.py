import os

shopping_list = [] #empty list or array

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help
    Enter 'SHOW' to show shopping list
    """)

def add_to_list(item): #function that appends items to shopping list
    shopping_list.append(item)
    #notify user that item was added state total number of items in lists
    print("Added! Your list has {} items total.".format(len(shopping_list)))
    show_list()

def show_list():
    clear_screen()
    print("Heres your list:")
    for item in shopping_list:
        print(item)


show_help() #begin program by printing show help to screen

while True: #infinite loop
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break #break out of loop with input done
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper == 'show':
        show_list()
        continue
    else:
    add_to_list(new_item)

show_list()
