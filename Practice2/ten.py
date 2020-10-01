def get_Max(a, b, c):
    def getMax(a , b):
        return max(a,b)
    return max(a, b , getMax(b, c))

