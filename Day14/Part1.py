# pokerface57 2023
# Python 3.11.1
# AOC Day 14 Part 1

def draw_board(board, min_y, max_y, min_x, max_x):
    for y in range(min_y, max_y):
        print(board[y][min_x:max_x])


bottom = 0


def draw_cave(board, string):
    string = string.split(' -> ')
    for i in range(len(string) - 1):
        x_start, y_start = string[i].split(',')
        x_finish, y_finish = string[(i + 1)].split(',')
        x_start = int(x_start)
        y_start = int(y_start)
        x_finish = int(x_finish)
        y_finish = int(y_finish)
        y_max = max(y_start, y_finish)
        global bottom
        if bottom < y_max:
            bottom = y_max
        if y_start == y_finish:
            if x_start < x_finish:
                for j in range(x_start, x_finish + 1):
                    board[y_start][j] = '#'
            else:
                for j in range(x_finish, x_start + 1):
                    board[y_start][j] = '#'

        else:
            if y_start < y_finish:
                for j in range(y_start, y_finish + 1):
                    board[j][x_start] = '#'
            else:
                for j in range(y_finish, y_start + 1):
                    board[j][x_start] = '#'
    return board


def sand_fall(board, bottom):
    block_elements = ['#', 'o']
    y_grain = 0
    x_grain = 500
    grain_count = 0
    while y_grain != bottom + 1:
        if board[y_grain][x_grain] not in block_elements:
            y_grain += 1
        else:
            if board[y_grain][x_grain - 1] not in block_elements:
                y_grain += 1
                x_grain -= 1
            else:
                if board[y_grain][x_grain + 1] not in block_elements:
                    y_grain += 1
                    x_grain += 1
                else:
                    board[y_grain - 1][x_grain] = 'o'
                    grain_count += 1
                    y_grain = 0
                    x_grain = 500

    return board, grain_count


with open('input.txt', 'r') as f:
    scan = f.read().split('\n')

depth = 180
width = 540
board = [['.' for i in range(width)] for i in range(depth)]
# draw_board(board, 0, 10, 493, 504)

for i in scan:
    board = draw_cave(board, i)

draw_board(board, 0, depth, 460, width)
print()
print('-' * 400)
print()
finish_board, result = sand_fall(board, bottom)
draw_board(finish_board, 0, depth, 460, width)
print()
print(f'Units of sand come to rest before sand starts flowing into the abyss below: {result}')
