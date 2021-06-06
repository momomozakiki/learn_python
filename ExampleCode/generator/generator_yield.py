import sys
import cProfile


nums_squared_lc = [i * 2 for i in range(10000)]
cProfile.run("[i * 2 for i in range(10000)]")
print("lc type : ", type(nums_squared_lc))
print(nums_squared_lc)
print("Objects size: ", sys.getsizeof(nums_squared_lc))

print()

nums_squared_gc = (i ** 2 for i in range(10000)) # if use () will consider as generator
cProfile.run("(i ** 2 for i in range(10000))")
print("gc type : ", type(nums_squared_gc))
print(nums_squared_gc)
print("Objects size: ", sys.getsizeof(nums_squared_gc))

