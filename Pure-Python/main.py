from constraint import *

problem = Problem()

cell_list = my_array = [x for x in range(80)]

# Add cells and all possible values
problem.addVariable(cell_list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Add constraints
# 1. All cells in a row must be different
for i in range(9):
    problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*9, i*9+9)])

# 2. All cells in a column must be different
for i in range(9):
    problem.addConstraint(AllDifferentConstraint(), [x for x in range(i, 81, 9)])

# 3. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27, i*3+j*27+3)] + [x for x in range(i*3+j*27+9, i*3+j*27+12)] + [x for x in range(i*3+j*27+18, i*3+j*27+21)])

# 4. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27+3, i*3+j*27+6)] + [x for x in range(i*3+j*27+12, i*3+j*27+15)] + [x for x in range(i*3+j*27+21, i*3+j*27+24)])


