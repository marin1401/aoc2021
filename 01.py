#Day 01

with open('./01.txt') as myinput:
    inputlines = myinput.readlines()

measurements = list(map(int, inputlines))

#Part 1

counter = 0
for current_measurement, next_measurement in zip(measurements, measurements[1:]):
    if next_measurement > current_measurement:
        counter += 1

print(counter)

#Part 2

counter = -1
current_sum = 0
for first_measurement, second_measurement, third_measurement in zip(measurements, measurements[1:], measurements[2:]):
    previous_sum = current_sum
    current_sum = first_measurement + second_measurement + third_measurement
    if current_sum > previous_sum:
        counter += 1

print(counter)