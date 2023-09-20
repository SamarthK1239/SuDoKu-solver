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

# Global Variables
problem = Problem()
cell_list = my_array = [x for x in range(80)]
solved = False
start_time = time.time()


# Functions
def solve_sudoku(sudoku):
    global solved
    global start_time
    start_time = time.time()
    while not solved:
        solve_cell(sudoku)
        if not solved:
            print("No solution found. Backtracking...")
            sudoku = backtrack(sudoku)
    print("Solved in " + str(time.time() - start_time) + " seconds.")
    return sudoku


def solve_cell(sudoku):
    global solved
    global start_time
    if not solved:
        print("Solving cell...")
        sudoku = compute_possibilities(sudoku)
        sudoku = find_least_possibilities(sudoku)
        if not solved:
            print("No solution found. Backtracking...")
            sudoku = backtrack(sudoku)
    return sudoku


def compute_possibilities(sudoku):
    global problem
    global cell_list
    print("Computing possibilities...")
    for i in range(81):
        if sudoku[i] == 0:
            problem.addVariable(cell_list[i], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        else:
            problem.addVariable(cell_list[i], [sudoku[i]])
    return sudoku


def find_least_possibilities(sudoku):
    global problem
    global solved
    global start_time
    print("Finding least possibilities...")
    least_possibilities = 10
    least_possibilities_cell = 0
    for i in range(81):
        if len(problem.getSolutions()) == 0:
            print("No solution found. Backtracking...")
            sudoku = backtrack(sudoku)
            return sudoku
        if sudoku[i] == 0:
            if len(problem.getSolutions()) < least_possibilities:
                least_possibilities = len(problem.getSolutions())
                least_possibilities_cell = i
    if least_possibilities == 10:
        print("Solved in " + str(time.time() - start_time) + " seconds.")
        solved = True
        return sudoku
    print("Solving cell " + str(least_possibilities_cell) + " with " + str(least_possibilities) + " possibilities...")
    sudoku[least_possibilities_cell] = problem.getSolutions()[0][least_possibilities_cell]
    problem = Problem()
    return sudoku


def backtrack(sudoku):
    global problem
    global solved
    global start_time
    print("Backtracking...")
    problem = Problem()
    for i in range(81):
        if sudoku[i] == 0:
            sudoku[i] = 0
        else:
            problem.addVariable(cell_list[i], [sudoku[i]])
    sudoku = backtrack_helper(sudoku)
    return sudoku


def backtrack_helper(sudoku):
    global problem
    global solved
    global start_time
    print("Backtracking helper...")
    for i in range(81):
        if sudoku[i] == 0:
            if len(problem.getSolutions()) == 0:
                print("No solution found. Backtracking...")
                sudoku = backtrack(sudoku)
                return sudoku
            else:
                print("Solving cell " + str(i) + " with " + str(len(problem.getSolutions())) + " possibilities...")
                sudoku[i] = problem.getSolutions()[0][i]
                problem = Problem()
                return sudoku
    print("Solved in " + str(time.time() - start_time) + " seconds.")
    solved = True
    return sudoku


solve_sudoku("070000043040009610800634900094052000358460020000800530080070091902100005007040802")
