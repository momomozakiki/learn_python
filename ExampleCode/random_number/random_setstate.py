import random

#print a random number:
print('Random number: ', random.random())

#capture the state:
state = random.getstate()
print("The capture state is: ", state)

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())
