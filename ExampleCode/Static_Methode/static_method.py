class Mathematics:
    def Add_Numbers(x, y):
        return x + y


# Create Add_Number static number
Mathematics.Add_Numbers = staticmethod(Mathematics.Add_Numbers)


print('The sum is: ', Mathematics.Add_Numbers(5, 10))