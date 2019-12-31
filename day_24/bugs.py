"""
Approaching Eris, dwarf planet named for the Greek goddes of discord

Eris is covered in bugs

Scan of planet is given by n x n grid (does n vary?)

Bugs represented by #, empty space represented by .
Edges can be assumed to be empty space

n = 5 for part 1 of the puzzle

Each minute, bugs are born, live, and die

Birth Conditions: bug is birthed in empty space if there is exactly 1 or 2 bugs adjacent
Death Conditions: bug dies unless it is adjacent to exactly 1 bug
Status Quo Conditions: all else
"""

from itertools import chain


def get_input_grid():
    """
    """
    pass


def get_surrounding_elements(input_grid, row, column):
    """
    Given a particular row and column of an input grid (2D Array)
    returns the values of the 4 adjacent elements in the 2D Array

    If the row and column values indicate an edge element, gives 
    a "." as an empty space.
    """

    if row - 1 >= 0:
        space_1 = input_grid[row - 1][column]
    else:
        space_1 = "."

    try:
        # will return index out of range error if edge space
        space_2 = input_grid[row + 1][column]
    except:
        space_2 = "."

    if column - 1 >= 0:
        space_3 = input_grid[row][column - 1]
    else:
        space_3 = "."

    try:
        # will return index out of range error if edge space
        space_4 = input_grid[row][column + 1]
    except:
        space_4 = "."

    return (space_1, space_2, space_3, space_4)


def process_cycle(input_grid):
    """
    """
    num_rows = len(input_grid)
    num_columns = len(input_grid[0])
    new_grid = [["." for y in range(num_columns)] for x in range(num_rows)]
    for row in range(num_rows):
        for column in range(num_columns):
            # print("Row: {}".format(row))
            # print("Column: {}".format(column))
            space = input_grid[row][column]
            surrounding_spaces = get_surrounding_elements(input_grid, row, column)
            # print("Surrounding Spaces: {}".format(surrounding_spaces))
            if space == ".":
                if surrounding_spaces.count("#") in (1, 2):
                    new_grid[row][column] = "#"
                else:
                    new_grid[row][column] = "."
            if space == "#":
                if surrounding_spaces.count("#") == 1:
                    new_grid[row][column] = "#"
                else:
                    new_grid[row][column] = "."

    return new_grid


def get_repeating_pattern(input_grid):
    """
    """
    pattern_found = False

    cycle = input_grid  # initiate current cyle
    traversed_cycles = [cycle]

    while pattern_found is not True:
        print("Current Cycle: {}".format(cycle))
        cycle = process_cycle(cycle)

        if cycle in traversed_cycles:
            return cycle
        else:
            traversed_cycles += [cycle]
            # print("traversed cycles: {}".format(traversed_cycles))

        # break  # for debugging


def flatten(array_2d):
    """
    Takes a 2D array defined as a list of lists and flattens it
    """
    array_1d = list(chain.from_iterable(array_2d))
    return array_1d


def biodiversity_rating(repeated_pattern):
    """
    """
    flattened_pattern = flatten(repeated_pattern)
    print(flattened_pattern)

    indexes = []
    while "#" in flattened_pattern:
        index = flattened_pattern.index("#")
        indexes += [index]
        flattened_pattern[index] = "."

    biodiversity = sum([2 ** index for index in indexes])

    return biodiversity


if __name__ == "__main__":
    # input_grid = get_input_grid('input.txt')  #TODO: get input file

    # For development purposes
    # input_grid = [
    #     [".", ".", ".", ".", "#"],
    #     ["#", ".", ".", "#", "."],
    #     ["#", ".", ".", "#", "#"],
    #     [".", ".", "#", ".", "."],
    #     ["#", ".", ".", ".", "."],
    # ]

    # Actual puzzle input
    input_grid = [
        ["#", "#", "#", ".", "#"],
        [".", ".", "#", ".", "."],
        ["#", ".", ".", "#", "."],
        ["#", ".", ".", ".", "."],
        [".", "#", ".", "#", "."],
    ]

    repeated_pattern = get_repeating_pattern(input_grid)

    print("Repeated Pattern: {}".format(repeated_pattern))

    biodiversity_rating = biodiversity_rating(repeated_pattern)

    print("Biodiversity Rating: {}".format(biodiversity_rating))
