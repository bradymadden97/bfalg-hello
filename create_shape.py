import random
import math


def create_shape(start_position, side_length=50.0):
    shape_sides = random.randint(3, 9)
    shape_angle = math.radians(180 - float((360 / shape_sides)))
    lines = [start_position[0], start_position[1]]
    current_angle = shape_angle
    flip = 1
    for side in range(shape_sides):
        x = lines[-1][0] + side_length * math.cos(current_angle) * flip
        y = lines[-1][1] + side_length * math.sin(current_angle) * flip
        lines.append([refine_value(x), refine_value(y)])
        current_angle += shape_angle
        flip *= -1
    return lines


def refine_value(val):
    return float("{:.3f}".format(val)) + 0.0
