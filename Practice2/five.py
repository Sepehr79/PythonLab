# define a function that calculates number of 'ali'
def count_Ali(text):
    counter = 0
    while text.__contains__("ali"):
        text = text.replace("ali", "", 1)
        counter += 1
    return counter


# input text from user
text = input()

# calculate number of 'ali'
number = count_Ali(text)
print(number)
