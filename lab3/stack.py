# Testing classes
class Stack:
    "LIFO Data Structure"
    def __init__(self):
        self.items = list()
    def push(self,elem):
        self.items.append(elem)
        return self.items
    def pop(self):
        elem = self[-1]
        del elem
        return elem

class SubclassStack(Stack):
    "Testing subclassing"
    def peek(self,elem):
        "peeking returns items from main stack"
        size = len(self.items)
        assert 0 <= elem < size
        return self.items[size-1-elem]

stk = SubclassStack()
check_doc_string = Stack()
print(check_doc_string.__doc__)
print(stk.__doc__)

stk.push("first element")
print(stk.push("second element"))

print(stk.peek(0)) # popped last element
print(stk.peek(1))


# If both the subclass and the superclass has a constructor, 
# then the object of the subclass is created through the constructor of the subclass.

# Python supports Multiple inheritance -> class DerivedClass(Base1, Base2): ..

# Class variables are shared across all objects while instance variables are for data unique to each instance. 
# Instance variable overrides the Class variables having same name which can accidentally introduce bugs or surprising behaviour in our code.

class Automobile:
    # Class variable is defined within our class and is shared by all instances of that class
    # below, vehicle is class variable:
    vehicle = 'Vehicle: car'
    def __init__(self,company) -> None:
        # These variables are going to be 'unique' to every instance of our class;
        # instance var:
        self.company = company
    def type(self,v):
        self.vehicle = v # instance variable
    def foo(self): 
        if self.vehicle == "Vehicle: not car": # this is making instance variable here and not calling class variable
            # on use via instance self.var search order is this: 1. instance 2.class 3. base class
            # on assigment -> self.var = .. this will always make an instance variable
            print(False)
car = Automobile('Ford')
aeroplane = Automobile('Not Ford su')
print(car.company)
print(car.vehicle) 
print(aeroplane.vehicle) # vehicle variable is same to both instances
print(aeroplane.company) # instance variables are different for both instances

# Mutable class variable: one copy shared by all e.g. 'vehicle' is shared by all instances
# Mutable instance variable: each instance has its own variable e.g. company is created for both car and aeroplane instances