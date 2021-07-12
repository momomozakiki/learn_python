def myfunc(n):
    return len(n)

def myfunc2(a, b):
    return a + b


tuple_item = ('apple', 'banana', 'cherry')
tuple_item2 = ('orange', 'lemon', 'pineapple')
x = map(myfunc, tuple_item)
y = map(myfunc2, tuple_item, tuple_item2)

print(x)
print(type(x))
print(tuple(x))

print()

print(y)
print(type(y))
print(tuple(y))

