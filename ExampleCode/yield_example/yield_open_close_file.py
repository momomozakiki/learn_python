
"""
https://stackabuse.com/python-context-managers
https://medium.com/@jkarma0920/python-with-context-managers-53fb10dae076
https://docs.python.org/3/reference/compound_stmts.html#with
https://docs.python.org/3/reference/datamodel.html#context-managers
https://docs.python.org/3/library/contextlib.html
https://rszalski.github.io/magicmethods/
advised we should use context managers when we see any of the following patterns in our code:
Open — Close
Lock — Release
Change — Reset
Enter — Exit
Start — Stop
"""
# https://www.geeksforgeeks.org/with-statement-in-python/

from contextlib import contextmanager


@contextmanager
def open_file(filename):
    opened_file = open(filename)
    try:
        print("Before yield: ")
        yield opened_file
        print("After yield: ")
    finally:
        print("Finally yield: ")
        opened_file.close()


with open_file('readme.txt') as managed_file:  # Assign open_file('readme.txt') to managed_file
    # print(type(managed_file))
    print("Before read text: ")
    text = managed_file.read()
    print(text)
    print("After print text")

with open_file('readme.txt') as managed_file2:  # Assign open_file('readme.txt') to managed_file
    # print(type(managed_file))
    print("Before read text: ")
    text = managed_file2.read()
    print(text)
    print("After print text")