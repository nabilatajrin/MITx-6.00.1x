secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
count = 0

def isWordGuessed(secretWord, lettersGuessed):
    for letters in secretWord:
        if letters in lettersGuessed:
            continue
        else:
            return False
    return True

print(isWordGuessed(secretWord, lettersGuessed))





