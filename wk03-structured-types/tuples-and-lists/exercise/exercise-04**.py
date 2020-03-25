aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'

print(aList)
print(bList)
print(aList == bList)

print(aList is bList)


cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)

print(cList)
print(dList)
print(cList == dList)
print(cList is dList)

"""Python has the two comparison operators == and is. At first sight they seem to be the same, 
but actually they are not. == compares two variables based on their actual value. In contrast, the is operator 
compares two variables based on the object id and returns True if the two variables refer to the same object."""