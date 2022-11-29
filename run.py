from random import randint

# Welcome message to start the game
print('-' * 65)
print("Welcome to play the Battleships Game with computer!")
print("You will have to find 5 battleships within the computer's grid.")
print("Battleships will be auto generated.")
print("Empty locations: o; Missed attempts: x; Hits: *")
print("Grid size is 5 x 5, choose integers between 1 and 5")
print('-' * 65)

player_name = input("Please enter your name: \n")
print('-' * 45)

player = []
computer = []
player_attempts = []

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

def player_attempt():
    """
    Player attempts on computer's grid by giving player's input.
    """
    print("\nChoose a row to hit the ship.")
    choose_row = int(input("For a row choose a number and press enter: \n"))
    print("\nChoose a column to hit the ship.")
    choose_col = int(input("For a column choose a number and press enter: \n"))
    if computer[choose_row][choose_col] == " @ ":
        player_attempts[choose_row][choose_col] = " * "
        print("\nWow...! You hit the ship :)\n")
    else:
        player_attempts[choose_row][choose_col] = " x "
        print("\nOh...! You missed the ship :(\n")
    print_grid(player_attempts)

def computer_attempt():
    """
    Computer attempts at player's grid using randomly generated co-ordinates.
    """
     # To generate the random numbers
    print("It's the computer's turn to choose!")
    choose_row = random_number(computer)
    choose_col = random_number(computer)
    print(f"\nComputer chose: ({choose_row}, {choose_col})")
    if player[choose_row][choose_col] == " @ ":
        player[choose_row][choose_col] = " * "
        print("\nOh...! Computer hit the ship :(")
    else:
        player[choose_row][choose_col] = " x "
        print("\nWow...! Computer missed the ship :)") 
    print("Player's grid:")
    print_grid(player)

def play_game():
    """
    The main function calling the other functions.
    """
    make_grid(player)
    make_grid(computer)
    make_grid(player_attempts)
    create_ship_location(player)
    create_ship_location(computer)

play_game()
player_attempt()
computer_attempt()