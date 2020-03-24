def fourthPower(x):
    '''
    x: int or float.
    '''

    def square(x):
        return x ** 2

    return square(square(x))

print(fourthPower(2))