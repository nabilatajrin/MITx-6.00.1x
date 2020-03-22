def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.4]
applyToEach(L, abs)
[1, 2, 3.4]
applyToEach(L, int)
[1, 2, 3]
applyToEach(L, fact)
[1, 2, 6]
applyToEach(L, fib)
[1, 2, 13]