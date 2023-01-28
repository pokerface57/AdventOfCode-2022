# pokerface57 2023
# Python 3.11.1
# AOC Day 9 Part 1

with open('input.txt', 'r') as f:
    move_H = []
    for line in f:
        move_H.append(line.strip().split())
move_H = list(map(lambda x: [x[0], int(x[1])], move_H))

# start point Head
x_H = x_H_now = 0
y_H = y_H_now = 0

# start point Tail
x_T = 0
y_T = 0

tail_coordinates = [[0, 0]]

for action in move_H:
    if action[0] == 'R':
        while x_H_now != x_H + action[1]:
            x_H_now += 1
            if x_H_now - x_T > 1 and y_H_now - y_T > 0:
                y_T += 1
                x_T += 1
                tail_coordinates.append([x_T, y_T])

            elif x_H_now - x_T > 1 and y_T - y_H_now > 0:
                y_T -= 1
                x_T += 1
                tail_coordinates.append([x_T, y_T])

            elif x_H_now - x_T > 1 and y_H_now == y_T:
                x_T += 1
                tail_coordinates.append([x_T, y_T])
        x_H = x_H_now

    elif action[0] == 'L':
        while x_H_now != x_H - action[1]:
            x_H_now -= 1
            if x_T - x_H_now > 1 and y_H_now - y_T > 0:
                y_T += 1
                x_T -= 1
                tail_coordinates.append([x_T, y_T])

            elif x_T - x_H_now > 1 and y_T - y_H_now > 0:
                y_T -= 1
                x_T -= 1
                tail_coordinates.append([x_T, y_T])

            elif x_T - x_H_now > 1 and y_H_now == y_T:
                x_T -= 1
                tail_coordinates.append([x_T, y_T])
        x_H = x_H_now

    elif action[0] == 'D':
        while y_H_now != y_H - action[1]:
            y_H_now -= 1
            if x_T - x_H_now > 0 and y_T - y_H_now > 1:
                y_T -= 1
                x_T -= 1
                tail_coordinates.append([x_T, y_T])

            elif x_H_now - x_T > 0 and y_T - y_H_now > 1:
                y_T -= 1
                x_T += 1
                tail_coordinates.append([x_T, y_T])

            elif y_T - y_H_now > 1 and x_H_now == x_T:
                y_T -= 1
                tail_coordinates.append([x_T, y_T])
        y_H = y_H_now

    else:
        while y_H_now != y_H + action[1]:
            y_H_now += 1
            if x_H_now - x_T > 0 and y_H_now - y_T > 1:
                y_T += 1
                x_T += 1
                tail_coordinates.append([x_T, y_T])

            elif x_T - x_H_now > 0 and y_H_now - y_T > 1:
                y_T += 1
                x_T -= 1
                tail_coordinates.append([x_T, y_T])

            elif y_H_now - y_T > 1 and x_H_now == x_T:
                y_T += 1
                tail_coordinates.append([x_T, y_T])
        y_H = y_H_now

# removing duplicate positions
result = [i for n, i in enumerate(tail_coordinates) if i not in tail_coordinates[:n]]
print(f'{len(result)} positions will visit the end of the rope')
