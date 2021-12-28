#Day 08

with open('./08.txt') as my_input:
    input_lines = my_input.readlines()

entries = [[values.split() for values in line.split('|')] for line in input_lines]

#Part 1

counter = 0
for input_values, output_values in entries:
    for value in output_values:
        if len(value) in (2, 3, 4, 7):
            counter += 1

print(counter)

#Part 2

def decode_values(values):
    values = [''.join(sorted(value)) for value in values]
    decoded_values = {number: None for number in range(10)}
    for value in values:
        if len(value) == 2:
            decoded_values[1] = value
        elif len(value) == 3:
            decoded_values[7] = value
        elif len(value) == 4:
            decoded_values[4] = value
        elif len(value) == 7:
            decoded_values[8] = value
    for value in values:
        if len(value) == 5:
            if len(set(decoded_values[1]).intersection(value)) == 2:
                decoded_values[3] = value
            elif len(set(decoded_values[4]).intersection(value)) == 2:
                decoded_values[2] = value
            else:
                decoded_values[5] = value
        elif len(value) == 6:
            if len(set(decoded_values[4]).intersection(value)) == 4:
                decoded_values[9] = value
            elif len(set(decoded_values[7]).intersection(value)) == 3:
                decoded_values[0] = value
            else:
                decoded_values[6] = value
    output = ''
    for value in values[-4:]:
        for decoded_value, coded_value in decoded_values.items():
            if value == coded_value :
                output += str(decoded_value)
    return int(output)

print(sum(decode_values(input_values + output_values) for input_values, output_values in entries))