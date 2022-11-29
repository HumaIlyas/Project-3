grid = []

def make_grid(grid):
    """
    Make the grid of " o " in the given empty list.
    Return a list containing 5 lists of letter " o "
    """
    for i in range(5):
        grid.append([" o "]*5)
    return grid

def print_grid(grid):
    """
    print the grid containing 5 lists of letter " o "
    """
    for ind in grid:
        print(" ".join(ind))

make_grid(grid)
print_grid(grid)