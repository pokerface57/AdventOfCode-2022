#  pokerface57 2023
# Python 3.11.1
# AOC Day 8 Part 1


count = 0  # inside trees


# row checking
def check_row(matr):
    index_invisible_trees = []
    for i in range(1, len(matr) - 1):
        for j in range(1, len(matr[i]) - 1):
            if matr[i][j] > max(matr[i][:j]) or matr[i][j] > max(matr[i][j + 1:]):
                global count
                count += 1
            else:
                index_invisible_trees.append([i, j])
    return index_invisible_trees  # index of invisible trees after row checking


# column checking
def check_column(matrix, l):
    bottom = []
    top = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if [i, j] in l:
                for k in range(i + 1, len(matrix)):
                    bottom.append(matrix[k][j])

                for k in range(0, i):
                    top.append(matrix[k][j])

                if matrix[i][j] > max(top) or matrix[i][j] > max(bottom):
                    global count
                    count += 1
                bottom = []
                top = []


# Create an array treeMatrix
with open('input.txt', 'r') as f:
    matrix = []
    for line in f.read().split('\n'):
        matrix += [[int(l) for l in line]]

# determining the maximum length of a row
max_long_str = 0
for i in matrix:
    if len(i) > max_long_str:
        max_long_str = len(i)

perimeter_trees_count = len(matrix[0]) + len(matrix[-1]) + ((len(matrix) - 2) * 2)

list_index_invisible_trees = check_row(matrix)

# add row 0 so that all rows are equal length
for i in range(0, len(matrix)):
    while len(matrix[i]) != max_long_str:
        matrix[i].append(0)

check_column(matrix, list_index_invisible_trees)

print('-' * 20)
print(f'Trees inside: {count}')
print(f'Trees outside: {perimeter_trees_count}')
res = perimeter_trees_count + count
print('-' * 20)
print(f'Result: {res}')
