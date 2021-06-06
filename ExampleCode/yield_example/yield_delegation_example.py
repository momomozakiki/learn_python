"""
Generators: The Final Frontier - Screencast
https://www.youtube.com/watch?v=5-qadlG7tWo
"""

def chain(x, y):
    yield from x
    yield from y

a = [1, 2, 3]
b = [4, 5, 6]
for x in chain(a, b):
    print(x, end=' ')

print()

for x in chain(a, b):
    # print(x)
    print(x, end='-')

print()

c = [7, 8, 9]
for x in chain(a, chain(b, c)):
    print(x, end=' ')

print()

for x in chain(chain(a, b), c):
    print(x, end=' ')