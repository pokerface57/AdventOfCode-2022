#  pokerface57 2023
# Python 3.11.1
# AOC Day 8 Part 2

# Create an array treeMatrix
with open('input.txt', 'r') as f:
    matrix = []
    for line in f.read().strip('\n').split('\n'):
        matrix += [[int(l) for l in line]]

max_view_points = 0
# checking every tree
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
        view_left = 0
        for k in range(j - 1, -1, -1):
            if matrix[i][j] > matrix[i][k]:
                view_left += 1
            elif matrix[i][j] <= matrix[i][k]:
                view_left += 1
                break

        view_right = 0
        for k in range(j + 1, len(matrix[i])):
            if matrix[i][j] > matrix[i][k]:
                view_right += 1
            elif matrix[i][j] <= matrix[i][k]:
                view_right += 1
                break

        view_bottom = 0
        for k in range(i + 1, len(matrix)):
            if matrix[i][j] > matrix[k][j]:
                view_bottom += 1
            elif matrix[i][j] <= matrix[k][j]:
                view_bottom += 1
                break

        view_top = 0
        for k in range(i - 1, -1, -1):
            if matrix[i][j] > matrix[k][j]:
                view_top += 1
            elif matrix[i][j] <= matrix[k][j]:
                view_top += 1
                break

        tree_view_points = view_left * view_right * view_top * view_bottom
        if tree_view_points > max_view_points:
            max_view_points = tree_view_points

print(f'The best view: {max_view_points} points')
