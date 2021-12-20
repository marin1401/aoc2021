#Day 01

with open('./01.txt') as my_input:
    input_lines = my_input.readlines()

measurements = list(map(int, input_lines))

counter_1, counter_2, current_sum = 0, -1, 0
for first_measurement, second_measurement, third_measurement in zip(measurements, measurements[1:], measurements[2:]):
    if second_measurement > first_measurement:
        counter_1 += 1
    previous_sum = current_sum
    current_sum = first_measurement + second_measurement + third_measurement
    if current_sum > previous_sum:
        counter_2 += 1

#Part 1

print(counter_1)

#Part 2

print(counter_2)
