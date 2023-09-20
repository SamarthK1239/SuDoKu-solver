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

# 5. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27+6, i*3+j*27+9)] + [x for x in range(i*3+j*27+15, i*3+j*27+18)] + [x for x in range(i*3+j*27+24, i*3+j*27+27)])

# 6. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27, i*3+j*27+1)] + [x for x in range(i*3+j*27+9, i*3+j*27+10)] + [x for x in range(i*3+j*27+18, i*3+j*27+19)])

# 7. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27+1, i*3+j*27+2)] + [x for x in range(i*3+j*27+10, i*3+j*27+11)] + [x for x in range(i*3+j*27+19, i*3+j*27+20)])

# 8. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27+2, i*3+j*27+3)] + [x for x in range(i*3+j*27+11, i*3+j*27+12)] + [x for x in range(i*3+j*27+20, i*3+j*27+21)])

# 9. All cells in a 3x3 square must be different
for i in range(3):
    for j in range(3):
        problem.addConstraint(AllDifferentConstraint(), [x for x in range(i*3+j*27+3, i*3+j*27+4)] + [x for x in range(i*3+j*27+12, i*3+j*27+13)] + [x for x in range(i*3+j*27+21, i*3+j*27+22)])



