#input and output

#ask for users name
name = input("what is your name? ")

#welcome user with name
print("Hi {}, get ready to play madlibs!".format(name))

verb = input("Please enter a verb:  ")
noun = input("Please enter a noun:  ")
adjective = input("Please enter a adjective:  ")

print("I enjoy running. I find it helps me to", verb, "better.")
print("without running, my", noun, "would probably not even work.")
print("My speed is getting more", adjective, "every single day!")
