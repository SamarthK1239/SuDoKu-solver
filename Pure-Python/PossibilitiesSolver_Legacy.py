# Solution Overview:
# Take a given sudoku starting state
# Compute all possibilities for each cell
# Find the one with the least possibilities
# Solve that cell
# Repeat with the updated state
# Continue until solved

# Imports
from constraint import *
import copy
import time

input_puzzle = ("070040800"
                "000009634"
                "043610900"
                "094358000"
                "052460800"
                "000020530"
                "080902007"
                "070100040"
                "091005802")
input_puzzle_normal = "070000043040009610800634900094052000358460020000800530080070091902100005007040802"
expected_output = "679518243543729618821634957794352186358461729216897534485276391962183475137945862"


# The input String is the digits of the puzzle, left to right, top to bottom
# Convert the input string to a 9x9 array
def convert_input(input_string):
    output_array = []
    for i in range(9):
        output_array.append([])
        for j in range(9):
            output_array[i].append(int(input_string[i * 9 + j]))
    return output_array


converted = convert_input(input_puzzle_normal)


def check_column(converted_input, column):
    column_list_numbers = []
    for i in range(9):
        if converted_input[i][column] != 0:
            column_list_numbers.append(converted_input[i][column])

    return column_list_numbers


def check_row(converted_input, column):
    row_list_numbers = []
    for i in range(9):
        if converted_input[column][i] != 0:
            row_list_numbers.append(converted_input[column][i])

    return row_list_numbers


def check_grid(converted_input, row, column):
    grid_list_numbers = []
    for i in range(3):
        for j in range(3):
            if converted_input[row + i][column + j] != 0:
                grid_list_numbers.append(converted_input[row + i][column + j])

    return grid_list_numbers


def invert_numbers_to_possibilities(array):
    output = []
    for i in range(1, 10):
        if i not in array:
            output.append(i)
    return output


def get_possibilities_for_cell(converted_input, row, column):
    cell_coordinates = [row, column]
    column_list_numbers = check_column(converted_input, column)
    column_possibilities = invert_numbers_to_possibilities(column_list_numbers)
    row_list_numbers = check_row(converted_input, row)
    row_possibilities = invert_numbers_to_possibilities(row_list_numbers)
    grid_list_numbers = check_grid(converted_input, row - row % 3, column - column % 3)
    grid_possibilities = invert_numbers_to_possibilities(grid_list_numbers)

    # Check which values are shared between the three possibilities lists
    possibilities = []
    for i in range(1, 10):
        if i in column_possibilities and i in row_possibilities and i in grid_possibilities:
            possibilities.append(i)

    return possibilities
