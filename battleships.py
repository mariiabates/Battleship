#see the readme.md file for description and data 
import random

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
    results in a legal arrangement. Return a Boolean value."""  
    # Check if the ship goes beyond the playing field
    if column + length > 10 or row + length > 10:
        return False
    # Check if there're squares occupied by the ship that are not in open sea
    for i in range(length): 
        if horizontal and not is_open_sea(row, column + i, fleet):
                return False
        elif not horizontal and not is_open_sea(row + i, column, fleet):
                return False
    return True

def place_ship_at(row, column, horizontal, length, fleet):
    """Add a ship, specified by row, column, horizontal, and length to the fleet.
    Return a new fleet. N.B. The function is part of randomly_place_all_ships() and changes the input fleet to save on memory. 
    The input is not passed manually from main(), so we don't risk undesirable changes to the input."""
    fleet.append((row, column, horizontal, length, set()))
    return fleet 

def randomly_place_all_ships():
    """Make a random legal arrangement of 10 ships in the ocean. Return the fleet."""
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
    hits any of the ships of the fleet. Return a Boolean value."""
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
    N.B. The function modifies the input fleet to save on space.
    """
    s = ()
    for ship in fleet:
        if check_if_hits(row, column, [ship]):
            s = ship
            ind = fleet.index(ship)
            # Add coordinates of the square to the set of hits for the ship in fleet
            fleet[ind][4].add((row, column)) 
            s[4].add((row, column))
            break
    return (fleet, s)

def are_unsunk_ships_left(fleet):
    """Check if there are ships in the fleet that are still not sunk. Return a Boolean value."""
    for ship in fleet:
        if not is_sunk(ship):
            return True
    return False

def main():
    """Prompt the user to call out rows and columns of shots and outputs the responses of the computer iteratively until the game stops.
    Returns nothing. No visualisation.
    """
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0
    squares_taken = set()

    while not game_over:
        try:
            loc_str = input("Enter row and column to shoot (separated by space) or X to exit: ").split()   
            if loc_str[0] == "X":
                break
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            # Try to hit a ship at given row and column
            ship_hit = hit(current_row, current_column, current_fleet)[1]
            shots += 1
            if not ship_hit or (current_row, current_column) in squares_taken:
                print(f"Shooting at row {current_row}, column {current_column}. You missed!")
            elif is_sunk(ship_hit):
                ship_name = ship_type(ship_hit)
                print(f"You sank a {ship_name}!")
                squares_taken.add((current_row, current_column))
            else:
                print(f"Shooting at row {current_row}, column {current_column}. You have a hit!") 
                squares_taken.add((current_row, current_column))
        except(ValueError, IndexError):
            print("Oops! That wasn't a valid input. Try again...")
        if not are_unsunk_ships_left(current_fleet): 
            game_over = True
            print(f"Great job! You required {shots} shots to sink all ships.")

if __name__ == '__main__': 
   main()