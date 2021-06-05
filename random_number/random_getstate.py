import random

x = random.getstate()

for num in x:
    print(num)
    print(type(num))

print(x[1])

y = x[1]

for item in y:
    print(item)