def fib(x):
    """ Base cases:
    • Females(0) = 1
    • Females(1) = 1
     Recursive case
    • Females(n) = Females(n-1) + Females(n-2)"""
    """assumes x an int >= 0
    returns Fibonacci of x"""

    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


print(fib(5))