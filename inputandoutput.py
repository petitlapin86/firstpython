#input and output

#ask for users name
print("what is your name? ")

#welcome user with name
print("Hi {}, get ready to play madlibs!".format(name))

verb = input("Please enter a verb:  \n")
noun = input("Please enter a noun:  \n")
adjective = input("Please enter a adjective:  \n")

print("I enjoy running. I find it helps me to {} better. \n
        without running, my {} would probably not even work.
        My speed is getting more {} every single day!".format(verb, noun, adjective))
