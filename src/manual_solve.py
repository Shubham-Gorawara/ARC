#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

"""
Name = Shubham Gorawara
ID = 21251097
GitHub repository link = https://github.com/Shubham-Gorawara/ARC
"""

"""
References

1)
"""





def solve_aabf363d(x):

    """
    Required transformation: The color of the bottom left-most cell in the grid is captured, then that cell is turned black and all the other non-black cells are changed to the color of the bottom left-most cell that was captured earlier.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    corner_element = x[(x.shape[0]-1)][0]
    x = np.where(x == corner_element, 0, x)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]!=0:
                x[i][j] = corner_element

    return x



def solve_a79310a0(x):

    """
    Required transformation: All cells are displaced downwards along the y-axis by a unit of 1 and their color is changed from blue to red.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    y = np.zeros((x.shape[0], x.shape[1]), dtype=int)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]!=0:
                y[i+1][j] = 2

    return y



def solve_25ff71a9(x):

    """
    Required transformation: All cells are displaced downwards along the y-axis by a unit of 1.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    y = np.zeros((x.shape[0], x.shape[1]), dtype=int)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]!=0:
                y[i+1][j] = x[i][j]

    return y



def solve_3ac3eb23(x):

    """
    Required transformation: position of non-black cells in the first row and their colors are noted. Then in each following row, alternating 2 cells and 1 cell of each of those colors are placed till the end of the grid. The 2 cells are placed such that they are spaced by 1 unit around the respective cells in the first row and the 1 cell in placed in the same column as the respective cells in the first row.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    list_colors = []
    list_positions = []

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]!=0:
                list_colors.append(x[i][j])
                list_positions.append(j)

    for i in range(1, x.shape[0]):
        for j in range(x.shape[1]):
            if i%2 !=0:
                for k in range(len(list_colors)):
                    x[i][list_positions[k] - 1] = list_colors[k]
                    x[i][list_positions[k] + 1] = list_colors[k]

            else:
                for k in range(len(list_colors)):
                    x[i][list_positions[k]] = list_colors[k]

    return x




def solve_c1d99e64(x):

    """
    Required transformation: in rows and columns consisting of only black cells, the black cells are replaced by red cells.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    # Number of rows of red color that will be formed
    rows = 0

    # for rows
    for i in range(x.shape[0]):
        ct = 0
        for j in range(x.shape[1]):
            if x[i][j] == 0:
                ct += 1
        if ct == x.shape[1]:
            rows += 1
            for k in range(x.shape[1]):
                x[i][k] = 2 # color red

    # for columns and applying same code after transpose, except altering to account for number of black cells
    x = np.transpose(x)

    for i in range(x.shape[0]):
        ct = 0
        for j in range(x.shape[1]):
            if x[i][j] == 0:
                ct += 1
        if ct == x.shape[1] - rows: # since the cells will be red after changing color in rows, adjusting for number of black cells in row
            for k in range(x.shape[1]):
                x[i][k] = 2 # color red

    x = np.transpose(x) # Returning to original shape

    return x






def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})"
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals():
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)

def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""

    # Open the JSON file and load it
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)


def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()
