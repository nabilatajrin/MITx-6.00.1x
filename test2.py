# n = 5
#
# *
# **
# ***
# ****
# *****
#
# n = 3
#
# *
# **
# ***

var = input('enter number')

for num in range(0, int(var)):
    for x in range(0, num+1):
        print('*', end='')

    print('')