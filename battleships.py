#see the readme.md file for description and data 
import copy, random 
import numpy as np

def is_sunk(ship):
    """Check if the ship is sunk. Return a Boolean value."""
    hits_num = ship[4]
    ship_length = ship[3]
    return len(hits_num) == ship_length

def ship_type(ship):
    """Return type of the ship as a string."""
    ship_length = ship[3]
    ship_dict = {1: "submarine", 2: "destroyer", 3: "cruiser", 4: "battleship"}
    return ship_dict.get(ship_length)

def is_open_sea(row, column, fleet):
    """Check if the square given by row and column neither contains nor is adjacent to some ship in the fleet. 
    Return a Boolean value.
    """
    for ship in fleet:
        horizontal = ship[2]
        ship_row = ship[0]
        ship_col = ship[1]
        ship_len = ship[3]
        if horizontal and abs(ship_row - row) <= 1 and ship_col - 1 <= column <= ship_col + ship_len:
            return False
        if not horizontal and abs(ship_col - column) <= 1 and ship_row - 1 <= row <= ship_row + ship_len:
            return False
    return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """Check if addition of a ship to the fleet (specified by row, column, horizontal, and length) 
    results in a legal arrangement. 
    Return a Boolean value.
    """  
    # If ship goes beyond the playing field, return False
    if column + length > 10 or row + length > 10:
        return False
    # If at least one square occupied by ship is not in open sea, return False
    for i in range(length): 
        if horizontal and not is_open_sea(row, column + i, fleet):
                return False
        elif not horizontal and not is_open_sea(row + i, column, fleet):
                return False
    return True

def place_ship_at(row, column, horizontal, length, fleet):
    """Add a ship, specified by row, column, horizontal, and length to the fleet.
    Return a new fleet. N.B. The function changes the original fleet
    """
    fleet.append((row, column, horizontal, length, set()))
    return fleet 

def randomly_place_all_ships():
    """Make a random legal arrangement of 10 ships in the ocean. 
    This function makes use of the functions ok_to_place_ship_at and place_ship_at.
    Return a fleet.
    """
    fleet = []
    for length in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1):
        done = False
        while not done:
            row = random.randint(0, 9)
            column = random.randint(0, 9)
            horizontal = random.choice([True, False])
            if ok_to_place_ship_at(row, column, horizontal, length, fleet): 
                place_ship_at(row, column, horizontal, length, fleet)
                done = True
    return fleet

def check_if_hits(row, column, fleet):
    """Check if the shot of the human player at the square represented by row and column
    hits any of the ships of the fleet.
    Return a Boolean value.
    """
    for ship in fleet:
        horizontal = ship[2]
        ship_row = ship[0]
        ship_col = ship[1]
        ship_len = ship[3]
        # Check if a horizontal ship was hit
        if horizontal and 0 <= (column - ship_col) < ship_len and ship_row == row:
            return True
        # Check if a vertical ship was hit
        elif not horizontal and 0 <= (row - ship_row) < ship_len and ship_col == column:
            return True
    return False
        
def hit(row, column, fleet): 
    """Perform a hit in the fleet at the square represented by row and column. 
    Return a tuple (fleet1, ship) where ship is the ship from the fleet and fleet1 is the fleet resulting from this hit.
    """
    s = ()
    new_fleet = copy.deepcopy(fleet)
    for ship in fleet:
        if check_if_hits(row, column, [ship]):
            s = ship
            ind = fleet.index(ship)
            # Add a square to the set of hits for the ship in fleet
            new_fleet[ind][4].add((row, column)) 
            s[4].add((row, column))
            break
    return (new_fleet, s)

def are_unsunk_ships_left(fleet):
    """Check if there are ships in the fleet that are still not sunk. Return a Boolean value."""
    for ship in fleet:
        if not is_sunk(ship):
            return True
    return False

def build_field():
    field = np.zeros(dtype=int, shape=(10,10))
    return field
    
def update_field(field, row, col, action):
    if action == "miss": n = 1
    if action == "hit": n = 2
    if action == "sink": n = 3
    field[row, col] = n
    return field

def print_field(myfield):
    field = myfield.tolist()
    print(" | 0 1 2 3 4 5 6 7 8 9 ")
    print("-  - - - - - - - - - - ")
    for i in range(len(field)):
        print(f"{i}|", end="")
        for column in field[i]:
            if column == 1:
                print(" _", end="")
            elif column == 2:
                print(" x", end="")
            elif column == 3:
                print(" X", end="")
            else:
                print(" .", end="")
        print()
    print()

def main():
    """Prompt the user to call out rows and columns of shots 
    and outputs the responses of the computer iteratively until the game stops.
    (a) there must be an option for the human player to quit the game at any time, 
    (b) the program must never crash (i.e., no termination with Python error messages), whatever the human player does.
    Returns nothing.
    """
    current_fleet = randomly_place_all_ships()
    myfield = build_field()
    print_field(myfield)

    game_over = False
    shots = 0

    while not game_over:
        try:
            loc_str = input("Enter row and colum to shoot (separted by space) or X to exit: ").split()   
            if loc_str[0] == "X":
                break
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            # Try to hit at given coordinates
            ship_hit = hit(current_row, current_column, current_fleet)[1]
            shots += 1
            if not ship_hit:
                print("You missed!")
                update_field(myfield, current_row, current_column, "miss")
                print_field(myfield)
            elif is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
                update_field(myfield, current_row, current_column, "sink")
                print_field(myfield)
            else:
                print("You have a hit!") 
                update_field(myfield, current_row, current_column, "hit")
                print_field(myfield)
        except(ValueError, IndexError):
            print("Oops! That was not a valid input. Try again...")
        if not are_unsunk_ships_left(current_fleet): 
            game_over = True
            print("Game over! You required", shots, "shots.")

if __name__ == '__main__': 
   main()

   # tkinter