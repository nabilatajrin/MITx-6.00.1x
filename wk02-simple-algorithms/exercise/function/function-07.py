def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

print(foo(5))