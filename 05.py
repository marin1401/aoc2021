#Day 05

with open('./05.txt') as my_input:
    input_lines = my_input.readlines()

coords = [[tuple(map(int, first_point.split(','))), tuple(map(int, second_point.split(',')))] for first_point, arrow, second_point in [line.split() for line in input_lines]]

field = [[0 for x in range(1000)] for y in range(1000)]

def count_overlaps(part):
    for coord in coords:
        (x1, y1), (x2, y2) = coord
        if part == 1:
            if x1 == x2:
                y1, y2 = sorted((y1, y2))
                for y in range(y1, y2+1):
                    field[y][x1] += 1
            elif y1 == y2:
                x1, x2 = sorted((x1, x2))
                for x in range(x1, x2+1):
                    field[y1][x] += 1
        if part == 2:
            dx = x2 - x1
            dy = y2 - y1
            for i in range(abs(dx) + 1):
                if dx < 0 and dy < 0:
                    field[y1-i][x1-i] += 1
                elif dx < 0 and dy > 0:
                    field[y1+i][x1-i] += 1
                elif dx > 0 and dy > 0:
                    field[y1+i][x1+i] += 1
                elif dx > 0 and dy < 0:
                    field[y1-i][x1+i] += 1
    counter = 0
    for row in field:
        for point in row:
            if point > 1:
                counter += 1
    return counter

#Part 1

print(count_overlaps(1))

#Part 2

print(count_overlaps(2))