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
