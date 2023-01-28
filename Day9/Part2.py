# pokerface57 2023
# Python 3.11.1
# AOC Day 9 Part 2

with open('input.txt', 'r') as f:
    move_H = []
    for line in f:
        move_H.append(line.strip().split())
move_H = list(map(lambda x: [x[0], int(x[1])], move_H))

# start point Head
x_H = x_H_now = 0
y_H = y_H_now = 0

# start point nodes
x_T = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = x_8 = x_9 = 0
y_T = y_2 = y_3 = y_4 = y_5 = y_6 = y_7 = y_8 = y_9 = 0

tail_coordinates = []


def move_H_and_1(action):  # node movement 1
    global x_H_now, x_H, y_H_now, y_H, y_T, x_T
    if action[0] == 'R':
        while x_H_now != x_H + action[1]:
            x_H_now += 1
            if x_H_now - x_T > 1 and y_H_now - y_T > 0:
                y_T += 1
                x_T += 1
                tail_coordinates.append(track_coordinates_9())  # adding tail coordinate after each step


            elif x_H_now - x_T > 1 and y_T - y_H_now > 0:
                y_T -= 1
                x_T += 1
                tail_coordinates.append(track_coordinates_9())

            elif x_H_now - x_T > 1 and y_H_now == y_T:
                x_T += 1
                tail_coordinates.append(track_coordinates_9())
        x_H = x_H_now

    elif action[0] == 'L':
        while x_H_now != x_H - action[1]:
            x_H_now -= 1
            if x_T - x_H_now > 1 and y_H_now - y_T > 0:
                y_T += 1
                x_T -= 1
                tail_coordinates.append(track_coordinates_9())

            elif x_T - x_H_now > 1 and y_T - y_H_now > 0:
                y_T -= 1
                x_T -= 1
                tail_coordinates.append(track_coordinates_9())

            elif x_T - x_H_now > 1 and y_H_now == y_T:
                x_T -= 1
                tail_coordinates.append(track_coordinates_9())
        x_H = x_H_now

    elif action[0] == 'D':
        while y_H_now != y_H - action[1]:
            y_H_now -= 1
            if x_T - x_H_now > 0 and y_T - y_H_now > 1:
                y_T -= 1
                x_T -= 1
                tail_coordinates.append(track_coordinates_9())

            elif x_H_now - x_T > 0 and y_T - y_H_now > 1:
                y_T -= 1
                x_T += 1
                tail_coordinates.append(track_coordinates_9())

            elif y_T - y_H_now > 1 and x_H_now == x_T:
                y_T -= 1
                tail_coordinates.append(track_coordinates_9())
        y_H = y_H_now

    else:
        while y_H_now != y_H + action[1]:
            y_H_now += 1
            if x_H_now - x_T > 0 and y_H_now - y_T > 1:
                y_T += 1
                x_T += 1
                tail_coordinates.append(track_coordinates_9())

            elif x_T - x_H_now > 0 and y_H_now - y_T > 1:
                y_T += 1
                x_T -= 1
                tail_coordinates.append(track_coordinates_9())

            elif y_H_now - y_T > 1 and x_H_now == x_T:
                y_T += 1
                tail_coordinates.append(track_coordinates_9())
        y_H = y_H_now


def move_nodes(coordinates1, coordinates2):  # node movement (2-9)
    x1 = coordinates1[0]
    y1 = coordinates1[1]
    x2 = coordinates2[0]
    y2 = coordinates2[1]

    if x1 - x2 > 1 and y1 == y2:
        x2 += 1

    elif x2 - x1 > 1 and y1 == y2:
        x2 -= 1

    elif y1 - y2 > 1 and x1 == x2:
        y2 += 1

    elif y2 - y1 > 1 and x1 == x2:
        y2 -= 1

    elif x1 - x2 > 1 and y1 - y2 > 0:
        x2 += 1
        y2 += 1

    elif x1 - x2 > 1 and y2 - y1 > 0:
        x2 += 1
        y2 -= 1

    elif x2 - x1 > 1 and y1 - y2 > 0:
        x2 -= 1
        y2 += 1

    elif x2 - x1 > 1 and y2 - y1 > 0:
        x2 -= 1
        y2 -= 1

    elif x2 - x1 > 0 and y1 - y2 > 1:
        x2 -= 1
        y2 += 1

    elif x1 - x2 > 0 and y1 - y2 > 1:
        x2 += 1
        y2 += 1

    elif x2 - x1 > 0 and y2 - y1 > 1:
        x2 -= 1
        y2 -= 1

    elif x1 - x2 > 0 and y2 - y1 > 1:
        x2 += 1
        y2 -= 1
    return x2, y2  # next node coordinates


def track_coordinates_9():
    global x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5, x_6, y_6, x_7, y_7, x_8, y_8, x_9, y_9
    x_2, y_2 = move_nodes([x_T, y_T], [x_2, y_2])
    x_3, y_3 = move_nodes([x_2, y_2], [x_3, y_3])
    x_4, y_4 = move_nodes([x_3, y_3], [x_4, y_4])
    x_5, y_5 = move_nodes([x_4, y_4], [x_5, y_5])
    x_6, y_6 = move_nodes([x_5, y_5], [x_6, y_6])
    x_7, y_7 = move_nodes([x_6, y_6], [x_7, y_7])
    x_8, y_8 = move_nodes([x_7, y_7], [x_8, y_8])
    x_9, y_9 = move_nodes([x_8, y_8], [x_9, y_9])
    return x_9, y_9  # tail coordinates


for i in move_H:
    move_H_and_1(i)

result = [i for n, i in enumerate(tail_coordinates) if i not in tail_coordinates[:n]]  # delete duplicate coordinates
print(f'{len(result)} positions will visit the end of the rope')
