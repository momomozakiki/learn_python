# Python program to demonstrate
# decorators

def msg_decorator(func):
    # Inner function
    def msg_wrapper(msg):
        print("A decorated line:", func(msg))

    return msg_wrapper


# Using the decorator
@msg_decorator
def print_name(name):
    return name


print_name("Pooventhiran")