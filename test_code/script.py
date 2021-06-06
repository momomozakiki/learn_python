import random as rad

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield rad.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield rad.randint(1, 15)

x = 1
for random_number in lottery():
    print("And the number %d is... %d!" % (x, random_number))
    x+= 1