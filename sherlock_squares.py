import math

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return max(0, end - start + 1)