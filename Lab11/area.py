import math

def circle(radius):
    if isinstance(radius, str):
        radius = float(radius)
    if radius <= 0:
        raise TypeError
    area = math.pi * (radius ** 2)
    return area

def square(side):
    if isinstance(side, str):
        side = float(side)
    if side <= 0:
        raise TypeError
    area = side ** 2
    return area

def rectangle(side1, side2):
    if isinstance(side1, str):
        side1 = float(side1)
    if isinstance(side2, str):
        side2 = float(side2)
    if (side1 <= 0) or (side2 <= 0):
        raise TypeError
    area = side1 * side2
    return area

def triangle(side1, side2):
    if isinstance(side1, str):
        side1 = float(side1)
    if isinstance(side2, str):
        side2 = float(side2)
    if (side1 <= 0) or (side2 <= 0):
        raise TypeError
    area = (side1 * side2) * 0.5
    return area