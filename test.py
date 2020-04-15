secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
count = 0

def isWordGuessed(secretWord, lettersGuessed):
    global count
    for i in range(0, len(secretWord)):
        for j in range(0, len(lettersGuessed)):
            if secretWord[i] == lettersGuessed[i]:
                count += 1
    if count == len(secretWord):
        print('True')
    else:
        print('False')

isWordGuessed(secretWord, lettersGuessed)





