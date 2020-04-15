Count=0
secretword='apple'
lettersguessed=['e','i','p','k','r','s']
def isWordGuessed(secretword, lettersguessed):
    global Count
    for i in range(0, len(secretword)):
        for j in range(0, len(lettersguessed)):
            if secretword[i] == lettersguessed[j]:
                Count = Count + 1
    if Count == len(secretword):
        print(True)
    else:
        print(False)
isWordGuessed(secretword, lettersguessed)