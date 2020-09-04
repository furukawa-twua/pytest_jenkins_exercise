import math

def CalcDistance (ax, ay, bx, by):
    return math.sqrt((bx - ax)**2 + (by - ay)**2)

def IsPrime (x):
    if x == 1: return False

    for k in range(2, int(math.sqrt(x)) + 1):
        if x % k == 0:
            return False

    return True
