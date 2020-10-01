# define a method that calculate max and min of arguments
def get_Max_Min(*args):
    maximum = args[0]
    minimum = args[0]
    for value in args:
        maximum = value if value > maximum else maximum
        minimum = value if value < minimum else minimum
    return maximum, minimum


