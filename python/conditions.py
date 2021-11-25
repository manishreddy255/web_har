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
