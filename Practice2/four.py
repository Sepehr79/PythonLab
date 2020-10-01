from datetime import date

# input date from user with ****/**/** format
input1 = input().split("/")
input2 = input().split("/")

# defining dates with date() method with year, month, day inputs
date1 = date(int(input1[0]), int(input1[1]), int(input1[2]))
date2 = date(int(input2[0]), int(input2[1]), int(input2[2]))

# print days between dates
print(date2 - date1)

