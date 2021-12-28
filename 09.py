#Day 09

from math import prod

with open('./09.txt') as my_input:
    input_lines = my_input.readlines()

points = [[int(point) for point in points.strip()] for points in input_lines]
horiz = len(points[0])
vert = len(points)

#Part 1

low_points = []
basins = {}
for y in range(vert):
    for x in range(horiz):
        up = points[y][x] < points[y-1][x] if y-1 > -1 else True
        down = points[y][x] < points[y+1][x] if y+1 < vert else True
        left = points[y][x] < points[y][x-1] if x-1 > -1 else True
        right = points[y][x] < points[y][x+1] if x+1 < horiz else True
        low_point = points[y][x] if all((up, down, left, right)) else None
        if low_point != None:
            low_points.append(low_point)
            basins[(x, y)] = [(x, y)]

print(sum(point + 1 for point in low_points))

#Part 2

def add_point_to_basin(new_coord, low_point, basins):
    if not any(new_coord in coords for coords in basins.values()):
        basins[low_point].append(new_coord)
        basin_sweep(new_coord, low_point, basins)

def basin_sweep(coord, low_point, basins):
    x, y = coord
    up = points[y-1][x] if y-1 > -1 else False
    down = points[y+1][x] if y+1 < vert else False
    left = points[y][x-1] if x-1 > -1 else False
    right = points[y][x+1] if x+1 < horiz else False
    if up and up != 9:
        add_point_to_basin((x, y-1), low_point, basins)
    if down and down != 9:
        add_point_to_basin((x, y+1), low_point, basins)
    if left and left != 9:
        add_point_to_basin((x-1, y), low_point, basins)
    if right and right != 9:
        add_point_to_basin((x+1, y), low_point, basins)

for coord in (low_point for low_point in basins.keys()):
    basin_sweep(coord, coord, basins)

print(prod(sorted(len(coords) for basin, coords in basins.items())[-3:]))