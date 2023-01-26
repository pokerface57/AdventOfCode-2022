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
    for i, j in l:
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
    for line in f.read().strip('\n').split('\n'):
        matrix += [[int(l) for l in line]]

perimeter_trees_count = len(matrix[0]) + len(matrix[-1]) + ((len(matrix) - 2) * 2)

list_index_invisible_trees = check_row(matrix)

check_column(matrix, list_index_invisible_trees)

print('-' * 20)
print(f'Trees inside: {count}')
print(f'Trees outside: {perimeter_trees_count}')
res = perimeter_trees_count + count
print('-' * 20)
print(f'Result: {res}')
