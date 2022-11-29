from random import randint

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

def random_number(grid):
    """
    Generate a random number between 0 and the length of the grid minus 1.
    The minus 1 is added in the argument because len starts at 1 but the grid's list start at 0.
    """
    return randint(0, len(grid)-1)

def create_ship_location(grid):
    """
    Create locations for battleships by using random co-ordinates.
    Update the grid with " @ " to indicate the location of the ships for the player's attempt to hit them.
    """
    for ind in range(0, 5):
        ship_row = random_number(grid)
        ship_col = random_number(grid)
        grid[ship_row][ship_col] = " @ "
        ind += 1

def play_game():
    """
    The main function calling the other functions.
    """
    make_grid(grid)
    create_ship_location(grid)
    print_grid(grid)

play_game()