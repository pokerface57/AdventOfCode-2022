# pokerface57 2023
# Python 3.11.1
# AOC Day 10 Part 1

with open('input.txt', 'r') as f:
    signal = []
    for line in f:
        signal.append(line.strip().split())

x = 1
cycle = 0
sum_signal_strength = 0

result_cycles = [20, 60, 100, 140, 180, 220]

for i in signal:
    if 'noop' in i:
        cycle += 1
        if cycle in result_cycles:
            sum_signal_strength += cycle * x
    else:
        cycle += 1
        if cycle in result_cycles:
            sum_signal_strength += cycle * x
        cycle += 1
        if cycle in result_cycles:
            sum_signal_strength += cycle * x
        x += int(i[1])

print(f'Sum of signal strengths: {sum_signal_strength}')
