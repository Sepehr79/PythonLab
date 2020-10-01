# get size of lists
count = int(input())

# get keys and values
keys = [input() for i in range(count)]
values = [int(input()) for i in range(count)]

# define dictionary
dic = {}

# insert keys and values into dictionary
for j in range(count):
    dic[keys[j]] = values[j]

print(dic)