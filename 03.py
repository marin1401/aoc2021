#Day 03

from collections import Counter

with open('./03.txt') as myinput:
    inputlines = myinput.readlines()

num_len = len(inputlines[0]) - 1

def find_most_common_bits(bit_position, report):
    nth_bits = []
    for number in report:
        nth_bits.append(number[bit_position])
    return Counter(nth_bits).most_common()

def get_new_candidates(bit_position, most_common_bit, candidates):
    new_candidates = []
    for number in candidates:
        if number[bit_position] == most_common_bit:
            new_candidates.append(number)
    return new_candidates

def get_ratings(gas):
    candidates = [number for number in inputlines]
    for bit_position in range(num_len):
        most_common, least_common = find_most_common_bits(bit_position, candidates)
        if most_common[1] == least_common[1]:
            if gas == 'o2':
                most_common_bit = '1'
            elif gas == 'co2':
                most_common_bit = '0'
        else:
            if gas == 'o2':
                most_common_bit = most_common[0]
            elif gas == 'co2':
                most_common_bit = least_common[0]
        candidates = get_new_candidates(bit_position, most_common_bit, candidates)
        if len(candidates) == 1:
            return candidates[0]

#Part 1

gamma_rate = ''
epsilon_rate = ''
for bit_position in range(num_len):
    most_common, least_common = find_most_common_bits(bit_position, inputlines)
    gamma_rate += most_common[0]
    epsilon_rate += least_common[0]

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

#Part 2

print(int(get_ratings('o2'), 2) * int(get_ratings('co2'), 2))
