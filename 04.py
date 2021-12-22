#Day 04

from itertools import chain

with open('./04.txt') as my_input:
    input_lines = my_input.read()

numbers = list(map(int, input_lines.split('\n\n')[0].split(',')))

boards_list = [list(map(int, number)) for number in [board.split() for board in input_lines.split('\n\n')[1:]]]
number_of_boards = len(boards_list)

boards_by_rows = [[row[i*5:i*5+5] for i in range(5)] for row in boards_list]
boards_by_columns = [[row[i::5] for i in range(5)] for row in boards_list]

zeros = [0, 0, 0, 0, 0]

def get_winning_board_score(boards_by_rows, boards_by_columns, number):
    for row_board, column_board in zip(boards_by_rows, boards_by_columns):
        if zeros in row_board:
            return sum(chain(*row_board))*number
        elif zeros in column_board:
            return sum(chain(*column_board))*number

def check_for_last_board(boards):
    counter = 0
    for board in boards:
        if sum(chain(*board)):
            counter += 1
        if counter > 1:
            return False
    return True

def get_last_board_score(last_board, boards, number):
    if last_board:
        for board in boards:
            score = sum(chain(*board))
            if score:
                return score*number
    return False

def get_score(boards_by_rows, boards_by_columns):
    winning_board = False
    for number in numbers:
        boards_by_rows = [[[0 if n==number else n for n in row] for row in board] for board in boards_by_rows]
        boards_by_columns = [[[0 if n==number else n for n in column] for column in board] for board in boards_by_columns]
        # Part 1
        if not winning_board:
            winning_board_score = get_winning_board_score(boards_by_rows, boards_by_columns, number)
            if winning_board_score:
                winning_board = True
                print(winning_board_score)
        # Part 2
        last_board_score = max(get_last_board_score(check_for_last_board(boards_by_rows), boards_by_rows, number),
                               get_last_board_score(check_for_last_board(boards_by_columns), boards_by_columns, number))
        if last_board_score:
            print(last_board_score)
            return
        for i in range(number_of_boards):
            if zeros in boards_by_rows[i] or zeros in boards_by_columns[i]:
                boards_by_rows[i] = [zeros for row in boards_by_rows[i]]
                boards_by_columns[i] = [zeros for column in boards_by_columns[i]]

get_score(boards_by_rows, boards_by_columns)