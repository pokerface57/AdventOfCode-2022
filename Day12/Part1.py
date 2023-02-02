# pokerface57 2023
# Python 3.11.1
# AOC Day 12 Part 1


from string import ascii_lowercase

all_letters = 'S' + ascii_lowercase + 'E'
possible_step = []
used_vertices = []

with open('test.txt', 'r') as f:
    labyrinth = []
    for line in f:
        labyrinth.append(list(line.strip()))
# search for a starting point
for i in range(0, len(labyrinth)):
    for j in range(0, len(labyrinth[i])):
        if labyrinth[i][j] == 'S':
            # the first argument is the row, the second argument is the column, the third attribute is the level
            start_point = [i, j, 0]
            # adding to the list of checked vertices
            possible_step.append(start_point)


def vertex_check(i, j, level):
    # remove a vertex from the beginning of the vertices being checked and add it to the end of the used vertices
    used_vertices.append(possible_step.pop(0))
    current_letter = labyrinth[i][j]
    if current_letter == 'E':
        global steps_count
        steps_count = level
    # based on the current position of the vertex, which vertices will be possible to check
    if i == 0 and j == 0:
        indexes_letters_around = [[i + 1, j], [i, j + 1]]
    elif i == 0 and len(labyrinth[i]) - 1 > j > 0:
        indexes_letters_around = [[i + 1, j], [i, j + 1], [i, j - 1]]
    elif i == 0 and j == len(labyrinth[i]) - 1:
        indexes_letters_around = [[i + 1, j], [i, j - 1]]
    elif i == len(labyrinth) - 1 and j == 0:
        indexes_letters_around = [[i - 1, j], [i, j + 1]]
    elif i == len(labyrinth) - 1 and len(labyrinth[i]) - 1 > j > 0:
        indexes_letters_around = [[i - 1, j], [i, j + 1], [i, j - 1]]
    elif i == len(labyrinth) - 1 and j == len(labyrinth[i]) - 1:
        indexes_letters_around = [[i - 1, j], [i, j - 1]]
    elif len(labyrinth) - 1 > i > 0 and j == 0:
        indexes_letters_around = [[i - 1, j], [i, j + 1], [i + 1, j]]
    elif len(labyrinth) - 1 > i > 0 and j == len(labyrinth[i]) - 1:
        indexes_letters_around = [[i - 1, j], [i, j - 1], [i + 1, j]]
    else:
        indexes_letters_around = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
    # checking each nearest vertex whether it was possible to move there
    for k in indexes_letters_around:
        if all_letters.index(current_letter) == all_letters.index(labyrinth[k[0]][k[1]]) or abs(
                all_letters.index(current_letter) - all_letters.index(labyrinth[k[0]][k[1]])) == 1:
            flag = False  # flag
            # search for a checked vertex in the list of already checked vertices
            for l in used_vertices:
                if [k[0], k[1]] == [l[0], l[1]]:
                    flag = True
            # search for a checked vertex in the list of already added vertices
            for l in possible_step:
                if [k[0], k[1]] == [l[0], l[1]]:
                    flag = True
            if flag == False:
                possible_step.append([k[0], k[1], level + 1])
    print(f'DEBUG: {current_letter, i ,j}')
    return current_letter


def main():
    global steps_count
    while len(possible_step) != 0:
        # checking the first vertex in the list of possible moves
        if vertex_check(possible_step[0][0], possible_step[0][1], possible_step[0][2]) == 'E':
            return f"Solution Found in {steps_count} steps"
    return f"No Solution Found!!!"


print(main())