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

