# Python program creating a context manager
# https://medium.com/@jkarma0920/python-with-context-managers-53fb10dae076

class ContextManager():
    def __init__(self):
        print('init methode called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit method called')


with ContextManager() as manager:
    print('with statement block')

print()
print(ContextManager)