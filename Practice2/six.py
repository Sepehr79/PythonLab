# define a dictionary
speed = {'jan': 47, 'Feb': 52, 'March': 47, 'April': 44, 'May': 52, 'June': 53, 'July': 54, 'Aug': 44, 'Sept': 54}

# define a list
list = []

# iterate values in speed dictionary and append them to the list
for value in speed.values():
    if value not in list:
        list.append(value)

print(list)
