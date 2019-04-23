#dictionary

#dictionaries are similar to lists however they arent sorted
#each dictionary has a key and a value


course = {"title": "learn python"}

#title is the key
#learn python is the value


#packing explained:
#takes a bunch of key value pairs and turns them into a dictionaries keys and values
#most useful in functions
def packer(**kwargs): #kwargs is 'keyword arguments'
    print(kwargs)

packer(name="kenneth", num=42, spanish_inquisition=none)


#unpacking

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("hi {} {}!".format(first_name, last_name))
    else:
        print("Hi, no name!")

unpacker(**{"last_name": "Jones", "first_name": "Paige"})


#iterating through a dictionary
#you can iterate through with a for loop
#example:
types_of_drinks = {"coffee": "black", "juice": "orange", "tea": "herbal"}


for key in types_of_drinks.keys():
    print(key)

for value in types_of_drinks.values():
    print(value)

#this is a tuple
for item in types_of_drinks.items():
    print(item)
