def iterPower(base, exp):
    count = 1
    result = base
    while count < exp:
        result *= base
        count += 1
    return result

print(iterPower(2, 3))