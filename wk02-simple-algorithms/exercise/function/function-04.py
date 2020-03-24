def foo(x, y=5):
    def bar(x):
        return x + 1

    return bar(y * 2)


print(foo(3))