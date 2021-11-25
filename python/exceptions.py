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
