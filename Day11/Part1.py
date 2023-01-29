# pokerface57 2023
# Python 3.11.1
# AOC Day 11 Part 1

monkey_0 = [65, 58, 93, 57, 66]
monkey_1 = [76, 97, 58, 72, 57, 92, 82]
monkey_2 = [90, 89, 96]
monkey_3 = [72, 63, 72, 99]
monkey_4 = [65]
monkey_5 = [97, 71]
monkey_6 = [83, 68, 88, 55, 87, 67]
monkey_7 = [64, 81, 50, 96, 82, 53, 62, 92]

inspected_items_mk_0 = 0
inspected_items_mk_1 = 0
inspected_items_mk_2 = 0
inspected_items_mk_3 = 0
inspected_items_mk_4 = 0
inspected_items_mk_5 = 0
inspected_items_mk_6 = 0
inspected_items_mk_7 = 0


def operation_0(things):
    for i in things:
        new = i * 7
        global inspected_items_mk_0
        inspected_items_mk_0 += 1
        new = new // 3
        if new % 19 == 0:
            monkey_6.append(new)
        else:
            monkey_4.append(new)
    things.clear()


def operation_1(things):
    for i in things:
        new = i + 4
        global inspected_items_mk_1
        inspected_items_mk_1 += 1
        new = new // 3
        if new % 3 == 0:
            monkey_7.append(new)
        else:
            monkey_5.append(new)
    things.clear()


def operation_2(things):
    for i in things:
        new = i * 5
        global inspected_items_mk_2
        inspected_items_mk_2 += 1
        new = new // 3
        if new % 13 == 0:
            monkey_5.append(new)
        else:
            monkey_1.append(new)
    things.clear()


def operation_3(things):
    for i in things:
        new = i ** 2
        global inspected_items_mk_3
        inspected_items_mk_3 += 1
        new = new // 3
        if new % 17 == 0:
            monkey_0.append(new)
        else:
            monkey_4.append(new)
    things.clear()


def operation_4(things):
    for i in things:
        new = i + 1
        global inspected_items_mk_4
        inspected_items_mk_4 += 1
        new = new // 3
        if new % 2 == 0:
            monkey_6.append(new)
        else:
            monkey_2.append(new)
    things.clear()


def operation_5(things):
    for i in things:
        new = i + 8
        global inspected_items_mk_5
        inspected_items_mk_5 += 1
        new = new // 3
        if new % 11 == 0:
            monkey_7.append(new)
        else:
            monkey_3.append(new)
    things.clear()


def operation_6(things):
    for i in things:
        new = i + 2
        global inspected_items_mk_6
        inspected_items_mk_6 += 1
        new = new // 3
        if new % 5 == 0:
            monkey_2.append(new)
        else:
            monkey_1.append(new)
    things.clear()


def operation_7(things):
    for i in things:
        new = i + 5
        global inspected_items_mk_7
        inspected_items_mk_7 += 1
        new = new // 3
        if new % 7 == 0:
            monkey_3.append(new)
        else:
            monkey_0.append(new)
    things.clear()


# current round
k = 0


def one_round():
    operation_0(monkey_0)
    operation_1(monkey_1)
    operation_2(monkey_2)
    operation_3(monkey_3)
    operation_4(monkey_4)
    operation_5(monkey_5)
    operation_6(monkey_6)
    operation_7(monkey_7)
    global k
    k += 1


while k != 20:
    one_round()

sort_inspected_items_mk = sorted(
    [inspected_items_mk_0, inspected_items_mk_1, inspected_items_mk_2, inspected_items_mk_3, inspected_items_mk_4,
     inspected_items_mk_5, inspected_items_mk_6, inspected_items_mk_7])

print(f'The level of monkey business: {sort_inspected_items_mk[-1] * sort_inspected_items_mk[-2]}')