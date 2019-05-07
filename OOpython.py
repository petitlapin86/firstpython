OO PYTHON
#these are magic methods - otherwise known as dunder


#What if our instances should be able to be used with mathematical operations? Let's define that!
#MATH MAGIC METHODS----------------------------
class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def __radd__(self, other):
        return self + other

    def __mul__(self, other): #should return the correct value type depending if the string represents a float or an int.
        if '.' in self.value: #check if its a float
            return float(self) * other #if so return this
        return int(self) * other #otherwise return this

    def __rmul__(self, other): #takes two arguments
        return self * other #returns them multiplied by each other

    def __imul__(self, other): #in the in-place method iadd, the value of self.value is updated before the return. The object value changes and is not just used to return a value
        self.value = self * other
        return self.value
