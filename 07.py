#Day 07

with open('./07.txt') as my_input:
    input_file = my_input.read()

positions = list(map(int, input_file.split(',')))

#Part 1

print(min(sum(abs(position - new_position) for position in positions) for new_position in range(max(positions))))

#Part 2

print(min(sum(abs(position - new_position)*(abs(position - new_position)+1)//2 for position in positions) for new_position in range(max(positions))))