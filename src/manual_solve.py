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

1) Numpy transpose docs - "https://numpy.org/doc/stable/reference/generated/numpy.transpose.html", accessed on 21th November 2021
2) Numpy numpy.zeroes docs - "https://numpy.org/doc/stable/reference/generated/numpy.zeros.html", accessed on 21th November 2021
3) Numpy numpy.where docs - "https://numpy.org/doc/stable/reference/generated/numpy.where.html", accessed on 21th November 2021
"""




def solve_aabf363d(x):

    """
    Required transformation: The color of the bottom left-most cell in the grid is captured, then that cell is turned black and all the other non-black cells are changed to the color of the bottom left-most cell that was captured earlier.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    corner_element = x[(x.shape[0]-1)][0] # Get the value (color) of the bottom left-most cell
    x = np.where(x == corner_element, 0, x) # Replace the bottom left-most cell value with 0

    for i in range(x.shape[0]): # Iterating over rows
        for j in range(x.shape[1]): # Iterating over columns
            if x[i][j]!=0:
                x[i][j] = corner_element # Change the color of the non-black cells to the color of the bottom left-most cell captured earlier

    return x




def solve_a79310a0(x):

    """
    Required transformation: All cells are displaced downwards  by a unit of 1 and their color is changed from blue to red.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    y = np.zeros((x.shape[0], x.shape[1]), dtype=int) # Creating a new numpy array with same shape as the original grid x and all black cells (value = 0)

    for i in range(x.shape[0]): # Iterating over rows
        for j in range(x.shape[1]): # Iterating over columns
            if x[i][j]!=0:
                # Change color of all blue cells, which are coded here as non-black cells to red, which is represented by value = 2, as was observed
                y[i+1][j] = 2 # And the cells are displaced downwards by 1 unit

    return y




def solve_3ac3eb23(x):

    """
    Required transformation: position of non-black cells in the first row and their colors are noted. Then in each following row, alternating 2 cells and 1 cell of each of those colors are placed till the end of the grid. The 2 cells in subsequent rows are placed such that they are spaced by 1 unit around their respective cells in the first row and the 1 cell placed in alternate rows is placed in the same column as their respective cells in the first row.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    list_colors = [] # initialising list to store value of the different colors
    list_positions = [] # initialising list to store y-coordinate of the different colored cells in the first row

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i][j]!=0:
                list_colors.append(x[i][j]) # Saving colors to the list of colors
                list_positions.append(j) # saving the y-coordinate i.e. column number of the colored cell to the list

    for i in range(1, x.shape[0]): # Iterating over rows starting with the 2nd row since the 1st row does not need to be operated upon
        for j in range(x.shape[1]): # Iterating over columns
            if i%2 !=0: # if odd indexed row then add 2 cells with the respective colors
                for k in range(len(list_colors)):
                    x[i][list_positions[k] - 1] = list_colors[k] # Assign same color as respective cell in first row to one unit position left than the column of cell in first row
                    x[i][list_positions[k] + 1] = list_colors[k] # Assign same color as respective cell in first row to one unit position right than the column of cell in first row

            else:   # if even indexed row then
                for k in range(len(list_colors)):
                    x[i][list_positions[k]] = list_colors[k] # Assign a single cell the same color and the same column as the respective cell in the first row

    return x




def solve_c1d99e64(x):

    """
    Required transformation: Examining the grid, in the rows and columns which consist of just all black cells, the black cells are replaced by red cells.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    # Number of rows of red color that will be formed initialised with 0
    rows = 0

    # for rows
    for i in range(x.shape[0]): # Iterating over rows
        ct = 0 # Variable to account for number of black cells in a row
        for j in range(x.shape[1]): # Iterating over columns
            if x[i][j] == 0:
                ct += 1
        if ct == x.shape[1]: # If all cells in a row are black
            rows += 1
            for k in range(x.shape[1]):
                x[i][k] = 2 # If all cells in a row are black then change the color of those cells to red which has value = 2 as seen by observation


    x = np.transpose(x) # To apply the same logic for columns, taking a transpose

    for i in range(x.shape[0]): # Iterating over rows
        ct = 0 # Variable to account for number of black cells in a row
        for j in range(x.shape[1]): # Iterating over columns
            if x[i][j] == 0:
                ct += 1
        if ct == x.shape[1] - rows: # After implementing first portion for rows, certain cells will be red, hence adjusting for number of black cells in row to account for new number of black cells
            for k in range(x.shape[1]):
                x[i][k] = 2 # If adjusted number of cells in a row are black then change the color of those cells to red which has value = 2 as seen by observation

    x = np.transpose(x) # Returning to original shape of the grid by taking another transpose

    return x




def solve_d4a91cb9(x):

    """
    Required transformation: The positions of the blue and red cells is captured. From observation, a path of yellow cells is formed from the blue to the red cell. The exact direction of the path including the vertical direction i.e. downwards or upwards from the blue cell depends on the position of the 2 cells relative to one another. 4 cases can exist in this scenario, which were coded using "if-elif" conditional statements.

    Grids solved correctly: All training and testing grids were solved correctly.
    """

    for i in range(x.shape[0]): # Iterating over rows
        for j in range(x.shape[1]): # Iterating over columns
            if x[i][j] == 8: # If blue cell detected saving its position as a tuple
                blue_position = (i,j)
            elif x[i][j] == 2:  # If red cell detected saving its position as a tuple
                red_position = (i,j)

    # Code path of yellow cells accordingly based on the 4 cases dependent on the relative positions of the blue and red cells to one another
    # yellow cell has value = 4 as seen by observation

    # Case 1:  x coordinate of blue cell < x coordinate of red cell and y coordinate of blue cell < y coordinate of red cell
    if (blue_position[0] < red_position[0]) and (blue_position[1] < red_position[1]):
        for i in range(blue_position[0]+1, red_position[0]+1):
            x[i][blue_position[1]] = 4
        for j in range(blue_position[1], red_position[1]):
            x[red_position[0]][j] = 4

    # Case 2:  x coordinate of red cell > x coordinate of blue cell and y coordinate of red cell < y coordinate of blue cell
    elif (red_position[0] > blue_position[0]) and (red_position[1] < blue_position[1]):
        for i in range(blue_position[0]+1, red_position[0]+1):
            x[i][blue_position[1]] = 4
        for j in range(red_position[1]+1, blue_position[1]+1):
            x[red_position[0]][j] = 4

    # Case 3:  x coordinate of red cell < x coordinate of blue cell and y coordinate of red cell > y coordinate of blue cell
    elif (red_position[0] < blue_position[0]) and (red_position[1] > blue_position[1]):
        for i in range(red_position[0], blue_position[0]):
            x[i][blue_position[1]] = 4
        for j in range(blue_position[1], red_position[1]):
            x[red_position[0]][j] = 4

    # Case 4:  x coordinate of red cell < x coordinate of blue cell and y coordinate of red cell < y coordinate of blue cell
    elif (red_position[0] < blue_position[0]) and (red_position[1] < blue_position[1]):
        for i in range(red_position[0], blue_position[0]):
            x[i][blue_position[1]] = 4
        for j in range(red_position[1]+1, blue_position[1]+1):
            x[red_position[0]][j] = 4

    return x




def solve_ac0a08a4(x):

    """
    Required transformation: The x & y dimensions of the original grid are multiplied by a factor of the number of distinct non-black colored cells in the original grid for eg: a 3x3 grid with 2 non-black colored cells is transformed to a grid of size 6x6. Then to adjust for the increase in dimensions, each cells color is replicated and increased by a factor of the square of the number of distinct non-black colors present in the original grid for eg: in a 3x3 grid with 2 non-black colored cells, each of the original cells will be replicated to now cover 4 cells in the form of a 2x2 grid.

    Grids solved correctly: All training and testing grids were solved correctly.

    """

    colors = [] # initialising list to store value of the different colors
    positions = [] # initialising list to store positions of the different colored cells in the first row

    for i in range(x.shape[0]): # Iterating over rows
        for j in range(x.shape[1]): # Iterating over columns
            if x[i][j]!=0:
                colors.append(x[i][j])  # Save value of the non-black colored cells to the colors list
                positions.append((i,j)) # Save the positions of the non-black colored cells as a tuple to the positions list

    distinct_colors = len(colors)   # Calculating the total number of distinct colors in the original grid

    # Creating a new numpy array with all black cells (value = 0) and adjusted shape by multiplying both the dimensions with the number of distinct colors in the original grid
    y = np.zeros((x.shape[0]*distinct_colors, x.shape[1]*distinct_colors), dtype=int)

    for i in range(distinct_colors):
        for j in range(distinct_colors):
            for k in range(distinct_colors):
                # Changing the colors of the specific cells obtained after adjusting the positions (stored in positions list), to have the respective colors (stored in the colors list)
                y[(positions[i][0]*distinct_colors) + j][(positions[i][1]*distinct_colors) + k] = colors[i]

    return y




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
