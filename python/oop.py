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
