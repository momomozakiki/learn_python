"""
https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod

To decide whether to use @staticmethod or @classmethod you have to look inside your method.
If your method accesses other variables/methods in your class then use @classmethod. On the other hand,
if your method does not touches any other parts of the class then use @staticmethod.

https://www.tutorialspoint.com/class-method-vs-static-method-in-python
"""


class Apple:
    _counter = 0

    @staticmethod
    def about_apple():
        print('Apple is good for you.')

        # note you can still access other member of the class
        # but you have to use the class instance
        # which is not very nice, because you have repeat yourself
        #
        # For example:
        # @staticmethod
        #    print('Number of apples have been juiced: %s' % Apple._counter)
        #
        # @classmethod
        #    print('Number of apples have been juiced: %s' % cls._counter)
        #
        #    @classmethod is especially useful when you move your function to other class,
        #       you don't have to rename the class reference

    @classmethod
    def make_apple_juice(cls, number_of_apples):
        print('Make juice:')
        for i in range(number_of_apples):
            cls._juice_this(i)

    @classmethod
    def _juice_this(cls, apple):
        print('Juicing %d...' % apple)
        cls._counter += 1


"""
cls._counter would still be cls._counter even if the code is put in a different class, 
or the class name is changed. Apple._counter is specific for the Apple class; 
for a different class, or when the class name is changed, 
you would need to change the referenced class. 
– kiamlaluno Nov 12 '19 at 22:55
"""
