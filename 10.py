#Day 10

with open('./10.txt') as my_input:
    input_lines = my_input.readlines()

navigation_subsystem = [line.strip() for line in input_lines]

legal = ['()', '[]', '{}', '<>']

corrupted = ['(]', '(}', '(>',
             '[)', '[}', '[>',
             '{)', '{]', '{>',
             '<)', '<]', '<}']

points = {'': 0, ')': 3, ']': 57, '}': 1197, '>': 25137}

def check_chunks(line, incorrect_chars, incomplete_lines):
    line_len = len(line)
    for chunk in legal:
        if chunk in line:
            line = line.replace(chunk, '')
    for chunk in corrupted:
        if chunk in line:
            incorrect_chars.append(chunk[1])
            return
    if line_len > len(line):
        return check_chunks(line, incorrect_chars, incomplete_lines)
    else:
        incomplete_lines.append(line)
        return

incorrect_chars, incomplete_lines = [], []
for line in navigation_subsystem:
    check_chunks(line, incorrect_chars, incomplete_lines)

#Part 1

print(sum(points[char] for char in incorrect_chars))

#Part 2

line_completions = [line[::-1] for line in incomplete_lines]

points = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for line in line_completions:
    total_score = 0
    for char in line:
        total_score *= 5
        total_score += points[char]
    scores.append(total_score)

print(sorted(scores)[(len(scores)-1)//2])