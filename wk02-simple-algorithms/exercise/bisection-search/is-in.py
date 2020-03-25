# c = 'c'
# s = 'gffdc'
#
# def isIn(c, s):
#     mid = len(s) // 2
#     if not len(s):
#         return False
#     elif c == s[mid]:
#         return True
#     elif c < s[mid]:
#         return isIn(c, s[:mid])
#     return isIn(c, s[mid + 1:])


print(isIn(c, s))