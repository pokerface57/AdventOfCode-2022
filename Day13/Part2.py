# pokerface57 2023
# Python 3.11.1
# AOC Day 13 Part 2

from ast import literal_eval

with open('input.txt', 'r') as f:
    packets = f.read().split('\n')
    packets = list(filter(None, packets))


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
        if result is None:
            continue
        return result


sorted_list = [[[2]], [[6]]]
for packet in packets:
    right = literal_eval(packet)
    for index, left in enumerate(sorted_list):
        if not comparison(left, right):
            sorted_list.insert(index, right)
            break
    if right not in sorted_list:
        sorted_list.append(right)

index_first_divider_packet = sorted_list.index([[2]]) + 1
index_second_divider_packet = sorted_list.index([[6]]) + 1
print(f'Decoder key: {index_first_divider_packet * index_second_divider_packet}')
