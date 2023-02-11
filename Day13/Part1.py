# pokerface57 2023
# Python 3.11.1
# AOC Day 13 Part 1

from ast import literal_eval

with open('input.txt', 'r') as f:
    packets = f.read().split('\n\n')


def comparison(left, right):
    for i in range(max(len(left), len(right))):
        if i > len(left) - 1:
            return True
        elif i > len(right) - 1:
            return False

        left_element = left[i]
        right_element = right[i]
        if isinstance(left_element, int) and isinstance(right_element, int):
            if left_element < right_element:
                return True
            elif left_element > right_element:
                return False
            else:
                continue
        elif isinstance(left_element, int):
            left_element = [left_element]
        elif isinstance(right_element, int):
            right_element = [right_element]

        result = comparison(left_element, right_element)
        if result == None:
            continue
        return result


count = 0
for packet_index, packet in enumerate(packets):
    left, right = packet.split('\n')
    left = literal_eval(left)
    right = literal_eval(right)
    if comparison(left, right):
        count += packet_index + 1

print(f'Sum of indices of correct pair: {count}')
