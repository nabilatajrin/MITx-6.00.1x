x = int(input('Enter an integer: '))
guess = 0
while guess**3 < x:
    guess += 1
    if guess**3 != x:
        print(str(x) + ' is not a perfect cube')
    else:
        print('Cube root of ' + str(x) + ' is ' + str(guess))
