# pokerface57 2023
# Python 3.11.1
# AOC Day 15 Part 1

from nums_from_string import get_nums


def path_calculation(list):
    sensor_x, sensor_y, beacon_x, beacon_y = list
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    return distance


def draw_line(list, y_line):
    sensor_x, sensor_y, beacon_x, beacon_y = list
    sensor_x = sensor_x + 100000  # increase 'x' so that the numbers do not fall into the negative range
    beacon_x = beacon_x + 100000
    distance = path_calculation(list)
    global line
    if beacon_y == y_line:
        line[beacon_x] = 'B'
    if y_line in range(sensor_y - distance, sensor_y + distance + 1):
        if sensor_y == y_line:
            line[sensor_x] = 'S'
            for i in range(sensor_x - distance, sensor_x + distance + 1):
                if line[i] == '.':
                    line[i] = '#'
        else:
            coefficient = abs(sensor_y - y_line)
            for j in range(sensor_x - distance + coefficient, sensor_x + distance + 1 - coefficient):
                if line[j] == '.':
                    line[j] = '#'


line = list('.' * 10000000)  # increase list so that the numbers do not fall into the negative range

with open('input.txt', 'r') as f:
    strings = f.read().split('\n')
    coordinates = []
    for i in strings:
        coordinates.append(get_nums(i))

for i in coordinates:
    draw_line(i, 2000000)

print(f'Positions cannot contain a beacon: {line.count("#")}')
