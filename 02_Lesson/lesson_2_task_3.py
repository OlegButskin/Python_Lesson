import math
def square(side):
    return math.ceil(side * side)

side_len = 10
zone = square(side_len)

print(f"Площадь квадрата {side_len} = {zone}")
