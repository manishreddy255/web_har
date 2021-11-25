def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

# so decorator is takes a functions and adds some functionality to it
# and return

# it happens in this way
# we keep a wrapper function in that we implement the given function and we return the
# wrapper function


@announce
def hello():
    print("Hello World")

# here announce will be the wrapper it takes teh hello
# and send it to the wrapper and then there we do something and also implement
# the hello function and return it


hello()
