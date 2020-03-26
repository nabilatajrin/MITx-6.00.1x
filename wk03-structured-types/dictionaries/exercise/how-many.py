animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)


def how_many(aDict):
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

print(how_many(animals))