#loops

#ask user for name
name = input("What is your name? ")

#ask the user by name if they understand while loops
understanding = input("{}, do you understand python while loops?\n (Enter yes/no)".format(name))

#check if the user doesnt understand while loops. also converts input to lowercase so YES == yes
while understanding.lower() != 'yes':
    #since the user doesnt understand while loops lets explain
    print("Okay, {}, while loops in python repeat as long as a certain boolean condition is met.".format(name))

    understanding = input("{}, now do you understand python while loops?\n (Enter yes/no)".format(name))

print("Thats great {}. I am pleased that you understand while loops now, that was getting repetitive.".format(name))
