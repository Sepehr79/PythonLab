# number of inputs
num = int(input())

# define lists
list1 = [int(input()) for i in range(num)]
list2 = [int(input()) for j in range(num)]

# define ansList
ansList = []

# append integers to ans list
for i in range(num):
    ansList.append(list2[i] if i % 2 == 0 else list1[i])


print(ansList)

