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
expected_output = "679518243543729618821634957794352186358461729216897534485276391962183475137945862"


# The input String is the digits of the puzzle, left to right, top to bottom
# Convert the input string to a 9x9 array
def convert_input(input_string):
    string = []
    for i in range(9):
        string.append(input_string[i*9:i*9+9])

    print(string)
    puzzle = []
    for i in range(9):
        puzzle.append([])
        for j in range(9):
            puzzle[i].append(int(string[i][j]))
    return puzzle




print(convert_input(input_puzzle))
