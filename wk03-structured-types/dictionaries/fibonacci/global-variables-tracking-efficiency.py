# def fib_efficient(n, d):
#     if n in d:
#         return d[n]
#     else:
#         ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#         d[n] = ans
#         return ans
#
# d = {1:1, 2:2}
# print(fib_efficient(6, d))
#
#
# def fib(n):
#     global numFibCalls
#     numFibCalls += 1
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n-1)+fib(n-2)
#
#
# def fibef(n, d):
#     global numFibCalls
#     numFibCalls += 1
#     if n in d:
#         return d[n]
#     else:
#         ans = fibef(n-1,d)+fibef(n-2,d)
#         d[n] = ans
#         return ans
#
#
# numFibCalls = 0
# print(fib(12))
# print('function calls', numFibCalls)
# numFibCalls = 0
# d = {1:1, 2:2}
# print(fib_efficient(12, d))
# print('function calls', numFibCalls)