# input size of list
count = int(input())

# input list members in **each** line
list = [int(input()) for i in range(count)]

# define a set and push list to remove duplicate elements
set = set(list)

# define a tuple and push set
tuple = tuple(set)

# print max and min
print("Max: {}".format(max(tuple)))
print("Min: {}".format(min(tuple)))
