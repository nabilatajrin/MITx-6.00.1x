# find out x
x = int(input('Please think of a number between 0 and 100!: '))

secret_number = 50
print("Is your secret number" + str(secret_number) + "?")

# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate
# I guessed correctly.
ans_1 = input('Enter h, l or c: ')

if ans_1 == 'h':
    secret_number = secret_number * 0.75
    print('Is your secret number ' + str(secret_number) + '?')

elif ans_1 == 'l':
    secret_number = secret_number * 1.25
    print('Is your secret number' + str(secret_number) + '?')

elif ans_1 == 'c':
    print('Is your secret number' + str(secret_number) + '?')

# loop

# epsilon = 0.01
# numGuesses = 0
# l = 1.0
# h = x
# ans = (h + l)/2.0
# while abs(ans**2 - x) >= epsilon:
#     print('low = ' + str(l) + ' high = ' + str(h) + ' ans = ' + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses = ' + str(numGuesses))
# print(str(ans) + ' is close to square root of ' + str(x))