def quotient_and_remainder(x, y):
    q = x//y
    r = x%y
    return (q, r)
(quot, rem) = quotient_and_remainder(4,5)

print(quotient_and_remainder(quot, rem))