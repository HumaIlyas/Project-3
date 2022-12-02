from random import randint
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Welcome message to start the game
print(Fore.WHITE + '-' * 35)
print(Fore.WHITE + "Welcome to play Battleships Game!")
print("Grid size: 5 x 5")
print("Choose integers between 1 and 5")
print("Number of battleships: 5")
print("Battleships: auto generated")
print("Empty locations: o")
print("Missed attempts: x")
print("Hits: *")
print(Fore.WHITE + '-' * 35)

# global variables
player_score = 0
computer_score = 0
player_name = input(Fore.CYAN + "Please ENTER your name: \n" + Fore.MAGENTA)
print(Fore.WHITE + '-' * 35)

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
    There are 5 ships on the grid. 
    while loop is to ensure that there are 5 ships on the grid.
    variable ship_point is to check if the points are less than 5, it loops again. 
    """
    ship_point = 0
    while ship_point < 5:
        ship_point = 0
        ship_row = random_number(grid)
        ship_col = random_number(grid)
        grid[ship_row][ship_col] = " @ "
        
        # for total count of ship_point, look in each list of the grid, and count @
        for row in grid:
            ship_point += row.count(" @ ")

def create_grids():
    """
    To create grids for playing the game. 
    player grid for player's battleships that the computer will attempt to hit.
    computer grid with computer's battleships.
    player_attempts grid (version of computer grid) to enter the input of the player, 
    so that the locations of the computer's battleships remain hidden from the player.
    """
    make_grid(player)
    make_grid(computer)
    make_grid(player_attempts)
    create_ship_location(player)
    create_ship_location(computer)

def validate_coordinates(value):
    """
    If values are not between 1 and 5, raise an error and request for a new input number.
    """
    try:
        if int(value) > 5 or int(value) < 1:
            raise ValueError(
                "Your attempt is off-grid!"
            )
    except ValueError as e:
        print(Fore.WHITE + '-' * 35)
        print(Fore.RED + f"{e}")
        print(Fore.RED + "ENTER an integer between 1 and 5")
        print(Fore.WHITE + '-' * 35)
        return False
    return True

def player_attempt():
    """
    Player attempts on computer's grid by giving player's input.
    To check whether it is valid data or an already chosen number.
    To check whether the player hit a battleship and show the result of that attempt.
    """
    global player_name
    print(Fore.BLUE + "\nComputer's grid:\n")
    print_grid(player_attempts)
    repeat = True
    while repeat:
        # To check if the input data is valid
        while True:
            print(Fore.GREEN + "\nChoose a row to hit the ship.")
            choose_row = input(Fore.GREEN + "Choose a number and press ENTER: \n" + Fore.YELLOW)
            if validate_coordinates(choose_row):
                break
        while True:
            print(Fore.GREEN + "\nChoose a column to hit the ship.")
            choose_col = input(Fore.GREEN + "Choose a number and press ENTER: \n" + Fore.YELLOW)
            if validate_coordinates(choose_col):
                break
        print(f"\n{Fore.MAGENTA + player_name}" + Fore.CYAN + " " + "chose:" + Fore.YELLOW + " " + f"({int(choose_row)}, {int(choose_col)})")
        # minus 1 is included in the argument because the players enter a number between 1 and 5.
        choose_row = int(choose_row)-1
        choose_col = int(choose_col)-1
        # To check if the data is valid.
        if (player_attempts[choose_row][choose_col] == " x " or 
                player_attempts[choose_row][choose_col] == " * "):
            print(Fore.WHITE + '-' * 35)
            print(Fore.RED + "You chose same coordinates before.")
            print(Fore.RED + "please choose another number!")
            print(Fore.WHITE + '-' * 35)
        else:
            repeat = False
    # To check if the attempt is a hit or not and show the result.
    global player_score
    if computer[choose_row][choose_col] == " @ ":
        player_attempts[choose_row][choose_col] = " * "
        print(Fore.GREEN + "\nWow...! You hit the ship :)\n")
        player_score += 1
    else:
        player_attempts[choose_row][choose_col] = " x "
        print(Fore.RED + "\nOh...! You missed the ship :(\n")

def computer_attempt():
    """
    Computer attempts at player's grid using randomly generated co-ordinates.
    """
    repeat = True
    # To generate the random numbers
    choose_row = random_number(computer)
    choose_col = random_number(computer)
    # To check if the data is valid
    while repeat:
        if (player[choose_row][choose_col] == " x " or 
                player[choose_row][choose_col] == " * "):
            choose_row = random_number(computer)
            choose_col = random_number(computer)
        else:
            repeat = False
    # To show the player about the computer choice and result   
    print(Fore.BLUE + "\nComputer" + Fore.CYAN + " " + "chose:" + Fore.YELLOW + " " + f"({choose_row + 1}, {choose_col + 1})")
    global computer_score
    if player[choose_row][choose_col] == " @ ":
        player[choose_row][choose_col] = " * "
        print(Fore.RED + "\nOh...! Computer hit the ship :(")
        computer_score += 1
    else:
        player[choose_row][choose_col] = " x "
        print(Fore.GREEN + "\nWow...! Computer missed the ship :)") 

def attempt_winner(grid):
    """
    To sum up the number of times " * " (hit battleships) appear in the grid. 
    If " * " equal to 5 on plyer or computer grid, either player or computer won the game.
    """
    total = 0
    for list in grid:
        total += list.count(" * ")
    return total

def final_winner():
    """
    To find the final winner after ten attempts.
    To display the final reuslt and message to the player.
    """
    player_result = attempt_winner(player_attempts)
    computer_result = attempt_winner(player)
    if player_result > computer_result:
        print(Fore.GREEN + "\nCongratulations! you WON :)")
    elif player_result < computer_result:
        print(Fore.RED + "\nSorry! Computer WON :(")
    else:
        print(Fore.YELLOW + "\nGame is draw!")

def play_game():
    """
    The main loop for the attempts of the player and the computer.
    """
    create_grids()
    global player_name
    global player_score
    global computer_score
    i = 0
    while i < 10:
        print(f"{Fore.MAGENTA + player_name}" + Fore.CYAN + " " + f"this is the attempt {i + 1}/10")
        input(Fore.WHITE + "\nPress ENTER for your's attempt.")
        player_attempt()
        print_grid(player_attempts)
        print(Fore.WHITE + '-' * 35)
        input(Fore.WHITE + "Press ENTER for computer's attempt.")
        computer_attempt()
        print(f"\n{Fore.MAGENTA + player_name}'s grid:\n")
        print_grid(player)
        print(Fore.WHITE + '-' * 35)
        print(f"{Fore.MAGENTA + player_name}" + Fore.WHITE + " " + "after this attempt scores are:")
        print(f"{Fore.MAGENTA + player_name}:" + Fore.YELLOW + " " + f"{player_score};" + " " + Fore.BLUE + "Computer:" + Fore.YELLOW + " " + f"{computer_score}")
        print(Fore.WHITE + '-' * 35)
        i += 1
        if attempt_winner(player) == 5:
            i = 10
        elif attempt_winner(player_attempts) == 5:
            i = 10
    final_winner()
    print(Fore.WHITE + "\nGAME IS OVER!")
    print(Fore.GREEN + "\nContinue playing the game...")
    print(Fore.WHITE + "Click on the button" + " " + Fore.BLUE + "RUN PROGRAM")
    print(Fore.RED + "\nQUIT the game...")
    input(Fore.WHITE + "Press" + " " + Fore.BLUE + "ENTER")
    quit()

# To call the main function
play_game()