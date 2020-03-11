given_string = 'azcbobobegghakl'
word = 'bob'

import re
count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), given_string))

print(count)



word = "bob" #Add space at trailing and leading sides.
input_string = "azcbobobegghakl"


print("Word count : ",input_string.count(word))

suvocount = input_string.count("bob")
print(suvocount)