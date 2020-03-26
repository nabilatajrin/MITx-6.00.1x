my_dict = {}
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

# add an entry
grades['Sylvan'] = 'A'

# test if key in dictionary
'John' in grades
'Daniel' in grades

# delete entry
del(grades['Ana'])

print(grades)

# get an iterable that acts like a tuple of all keys
print(grades.keys())

# get an iterable that acts like a tuple of all values
print(grades.values())