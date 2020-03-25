def gcdRecur(a, b):

    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)

print(gcdRecur(5, 12))

# recursion problem....still doubt