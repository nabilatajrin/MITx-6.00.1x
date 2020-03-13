mysum = 0
for i in range(5, 11, 2):
    print(i)
    mysum += i
    if mysum == 5:
        break
    # mysum += i --same
print(mysum)


mysum2 = 0
for i in range(5, 11, 2):
    mysum2 += i
print(mysum2)