import math


def calc_distance(x, y):
    dist = math.sqrt((x) ** 2 + (y) ** 2)
    return dist


def calc_length(x_1, y_1, x_2, y_2):
    length = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return length


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
x3 = math.floor(float(input()))
y3 = math.floor(float(input()))
x4 = math.floor(float(input()))
y4 = math.floor(float(input()))
if calc_length(x1, y1, x2, y2) > calc_length(x3, y3, x4, y4):
    if calc_distance(x1, y1) < calc_distance(x2, y2):
        print(tuple((x1, y1)), tuple((x2, y2)), sep="")
    else:
        print(tuple((x2, y2)), tuple((x1, y1)), sep="")
elif calc_length(x1, y1, x2, y2) < calc_length(x3, y3, x4, y4):
    if calc_distance(x3, y3) < calc_distance(x4, y4):
        print(tuple((x3, y3)), tuple((x4, y4)), sep="")
    else:
        print(tuple((x4, y4)), tuple((x3, y3)), sep="")
else:
        print(tuple((x1, y1)), tuple((x2, y2)), sep="")