#Day 02

with open('./02.txt') as my_input:
    input_lines = my_input.readlines()

commands = [(direction, int(value)) for direction, value in [command.split() for command in input_lines]]

x, y, aim = 0, 0, 0
for direction, value in commands:
    if direction == 'forward':
        x += value
        y += value*aim
    elif direction == 'up':
        aim -= value
    elif direction == 'down':
        aim += value

#Part 1

print(x*aim)

#Part 2

print(x*y)
