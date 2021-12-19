#Day 02

with open('./02.txt') as myinput:
    inputlines = myinput.readlines()

commands = [command.split() for command in inputlines]
commands = [(direction, int(value)) for direction, value in commands]

#Part 1

x, y = 0, 0
for direction, value in commands:
    if direction == 'forward':
        x += value
    elif direction == 'up':
        y -= value
    elif direction == 'down':
        y += value

print(x*y)

#Part 2

x, y, aim = 0, 0, 0
for direction, value in commands:
    if direction == 'forward':
        x += value
        y += value*aim
    elif direction == 'up':
        aim -= value
    elif direction == 'down':
        aim += value

print(x*y)