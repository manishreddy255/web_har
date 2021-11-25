print("hello world")

# in python variables are

a = 28
b = 1.5
c = "hello"
d = True
e = None

# now let's take some input and type theri name

name = input("what is your name? ")

# print("hello", name)
print(f"Hello, {name}")

n = int(input("number: "))

# in python you need indentation it is strictly followed
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

# if you allow the program without any changes to run
# you will face error as the input taken is string
# although you entered is number but you need to explicitly
# convert it to int
#n = int(input("number: "))

# count a bunch of numbers in using loop

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(i)

# for i in range(10):
#     print(i)

# names = ["harry", "ron", "hermione", "ginny", "neville"]

# for i in names:
#     print(i)

# for i in names[0]:
#     print(i)

# defined a list of names
names = ["harry", "ron", "hermione", "ginny", "neville"]

print(names)
print(names[0])

# adds a value to the end of the list
names.append("Draco")

print(names)

# you can also sort the list with methods
names.sort()  # it modifiles the list
print(names)

# name = "manish"

# print(name[1])


# storing multiple name in an array
# in python that is called list

# name = ["manish", "kumar", "singh"]

# print(type(name))


######## Tuple ##############
# tuple is similar to list but it is immutable
# it is used where there are couple of values and we dont want to change the values

# coordinateX = 19.0
# coordinateY = 178.0

# coordinate = (10.0, 20.0)
# as they are immutable we cant change the values
# and we can access the values by index

######## Data Structure ##############
# list - sequence of mutable values
# tuple - sequence of immutable values
# dict - collection of key value pairs
# dictionaly is like an object in javascript
# set - collection of unique values
# string

# sets is unordered collection of unique elements
# create an empty set

s = set()

# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# print the set
print(s)

# remove 4  from set
s.remove(2)

print(s)

# no elements ever appear twice in a set

# how many elemnts are in the set
print(f"there are {len(s)} in")

# dict is used when you don't want order and you know keys are unqiue
# dict is mutable
# dict is unordered
# dict is not indexed

houses = {
    "harry": "Gryffindor",
    "Draco": "Slytherin",
}

print(houses)
print(houses["harry"])

for key in houses:
    print(key, houses[key])


# define our functions in python

def square(x):
    return x*x

# now we will see how we import a function from another file
# from functions import square
# the above statement says from functions file
# import the function square
# you could also do something lik this :
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")

# from functions import square
# the above statement says from functions file
# import the function square
# you could also do something lik this :
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")


# creating a class in python
# it's a template for a object

# class Point():
#     # when we create a point we need to place init in the class
#     # and in that we have to give self as a parameter
#     # and with that self only we create x and y type things
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2


# # creating a point object
# p = Point(2, 3)
# # accessing the data of the object
# print(p.x)
# print(p.y)

# airplane program

class Flight():
    # init that creates a capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # add a paassenger to flight depending on the open seats
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # open seat checks for capacity
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Draco"]

for person in people:
    # her we are adding passengers one by one in the flight
    # and storing the result to the variable success
    # and depending on that deciding if the passenger is added or not
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")


people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"},
]

# people.sort()


# def f(person):
#     return person["name"]

# # with this it look for key by going to the f function
# people.sort(key=f)

people.sort(key=lambda person: person["name"])
# here lambda is a function that takes a single argument

print(people)





import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

# result = x / y
# we don't want errors so we catch em
# this is called exception handler
try:
    result = x / y
except ZeroDivisionError:
    print("Division by zero is not allowed")
    sys.exit(1)  # it means exit with status code of 1

print(result)

# instead of try catch we have try except finally
