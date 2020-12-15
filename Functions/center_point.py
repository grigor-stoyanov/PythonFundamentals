import math


def calc_distance(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)
    return dist


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
if calc_distance(x1, y1) < calc_distance(x2, y2):
    x1 = round(x1)
    y1 = round(y1)
    print(tuple((x1, y1)))
else:
    x2 = round(x2)
    y2 = round(y2)
    print(tuple((x2, y2)))
