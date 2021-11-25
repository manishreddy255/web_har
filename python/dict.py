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
