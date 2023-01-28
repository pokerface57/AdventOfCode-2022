# pokerface57 2023
# Python 3.11.1
# AOC Day 10 Part 2

with open('input.txt', 'r') as f:
    signal = []
    for line in f:
        signal.append(line.strip().split())

x = 1
cycle = 0
sprite = '###.....................................'
row = ''
result = ''

for i in signal:
    if 'noop' in i:
        cycle += 1
        if sprite[cycle - 1] == '#':
            row += '#'
        else:
            row += ' '

        if len(row) == 40:
            result += row + '\n'
            cycle = 0
            row = ''


    else:
        cycle += 1
        if sprite[cycle - 1] == '#':
            row += '#'
        else:
            row += ' '

        if len(row) == 40:
            result += row + '\n'
            cycle = 0
            row = ''
        cycle += 1

        if sprite[cycle - 1] == '#':
            row += '#'
        else:
            row += ' '

        if len(row) == 40:
            result += row + '\n'
            cycle = 0
            row = ''
        x += int(i[1])

        a = '.' * (x - 1)   # first part of output sprite
        b = 40 - len(a)     # second part of output sprite
        sprite = f'{a}{"###":.<{b}}'

print(result)
