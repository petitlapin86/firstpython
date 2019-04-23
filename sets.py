#sets
#a set is a collection of items that belong together
#sets can be compared
#they are mutable like lists

#this is a set
numbers = {1,2,3}

#to add to a set
numbers.add(4)

#to update a set
numbers.update({5, 6, 7})

#to remove from a set (if the item doesnt exist it will error)
numbers.remove(4)

#to discard (which tries to remove the value, but if it doesnt exist just moves on)
numbers.discard(6)
