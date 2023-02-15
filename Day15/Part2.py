# pokerface57 2023
# Python 3.11.1
# AOC Day 15 Part 2

from shapely.ops import unary_union, clip_by_rect
from shapely.geometry import Polygon
from nums_from_string import get_nums


def path_calculation(list):
    sensor_x, sensor_y, beacon_x, beacon_y = list
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    return distance


upoly = Polygon()

with open('input.txt', 'r') as f:
    strings = f.read().split('\n')
    coordinates = []
    for i in strings:
        coordinates.append(get_nums(i))

for shape in coordinates:
    sensor_x, sensor_y, beacon_x, beacon_y = shape
    distance = path_calculation(shape)
    upoly = unary_union([upoly, Polygon(
        [(sensor_x, sensor_y + distance), (sensor_x - distance, sensor_y), (sensor_x, sensor_y - distance),
         (sensor_x + distance, sensor_y)])])

interior = clip_by_rect(upoly, 0, 0, 4000000, 4000000).interiors[0]
x, y = tuple(map(round, interior.centroid.coords[:][0]))
print(f'Tuning frequency: {x * 4000000 + y}')