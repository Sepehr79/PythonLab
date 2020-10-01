# input from user
nums = input().split(",")

# define list and add nums
list = []
list += nums

# define a tuple and add nums
tuple = tuple(list)

# print list and tuple
print("list: {}".format(list))
print("tuple: {}".format(tuple))

