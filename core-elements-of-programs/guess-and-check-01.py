x = int(input('Enter only a perfect square : '))
guess = 0
while guess**2 < x:
    guess += 1
print('Square root of ' + str(x) + ' is ' + str(guess))