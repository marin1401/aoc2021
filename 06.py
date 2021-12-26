#Day 06

from collections import Counter

with open('./06.txt') as my_input:
    input_file = my_input.read()

initial_state = list(map(int, input_file.split(',')))

def get_new_fish_birthdays(state, n, number_of_days, new_fish_birthdays):
    for birthday in range(state, number_of_days + 1, 7):
        if birthday in new_fish_birthdays:
            new_fish_birthdays[birthday] += 1*n
        else:
            new_fish_birthdays[birthday] = 1*n

def get_total_number_of_fish(number_of_days, new_fish_birthdays):
    for state, n in Counter(initial_state).items():
        get_new_fish_birthdays(state, n, number_of_days, new_fish_birthdays)
    new_fish = 0
    for day in range(number_of_days):
        if day in new_fish_birthdays:
            state = day + 9
            n = new_fish_birthdays[day]
            new_fish += n
            get_new_fish_birthdays(state, n, number_of_days, new_fish_birthdays)
    return len(initial_state) + new_fish

#Part 1

print(get_total_number_of_fish(80, {}))

#Part 2

print(get_total_number_of_fish(256, {}))