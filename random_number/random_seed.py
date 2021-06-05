# https://www.w3schools.com/python/module_random.asp
'''
random.seed(a, version)

a           	Optional. The seed value needed to generate a random number.
                If it is an integer it is used directly, if not it has to be converted into an integer.
                Default value is None, and if None, the generator uses the current system time.

version         An integer specifying how to convert the a parameter into a integer.
                Default value is 2
'''

import random

# Test 1
random.seed(10)         # Same value of seed will return same random value
print(random.random())

# Test 2
random.seed(10)         # Same value of seed will return same random value
print(random.random())

random.seed()
print(random.random())

random.seed()
print(random.random())