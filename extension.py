import battleships
import numpy as np

def build_field():
    """Create a starting playing field matrix. Return the field."""
    field = np.full(dtype="str", shape=(10,10), fill_value=".")
    return field
    
def update_field(field, row, col, hit_result, all_ship_squares=None, ship_name=None):
    """Update the field matrix based on the result of the hit. Return updated field."""
    if hit_result == "miss":
        field[row, col] = "_"
    if hit_result == "hit":
        field[row, col] = "x"
    if hit_result == "sink":
        rows, cols = zip(*all_ship_squares)
        field[rows, cols] = ship_name[0].upper()
    return field

def print_field(field):
    """Print the playing field matrix to the console."""
    print()
    print("  | 0 1 2 3 4 5 6 7 8 9 | ")
    print(" -  - - - - - - - - - -  -")
    for row in range(len(field)):
        print(f" {row}|", end="")
        for square in field[row]:
            print(f" {square}", end="")
        print(f" |{row}")
    print(" -  - - - - - - - - - -  -")
    print("  | 0 1 2 3 4 5 6 7 8 9 | ")
    print()

def main():
    """Prompt the user to call out rows and columns of shots and outputs the responses of the computer iteratively until the game stops.
    Returns nothing. Visualisation implementation.
    """
    current_fleet = battleships.randomly_place_all_ships()
    myfield = build_field()
    print_field(myfield)

    game_over = False
    shots = 0

    while not game_over:
        try:
            loc_str = input("Enter row and column to shoot (separated by space) or X to exit: ").split()   
            if loc_str[0] == "X":
                break
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            # Try to hit a ship at given row and column
            ship_hit = battleships.hit(current_row, current_column, current_fleet)[1]
            shots += 1
            if not ship_hit:
                print("You missed!")
                update_field(myfield, current_row, current_column, "miss")
                print_field(myfield)
            elif battleships.is_sunk(ship_hit):
                ship_name = battleships.ship_type(ship_hit)
                all_ship_squares = ship_hit[4]
                print(f"You sank a {ship_name} !")
                update_field(myfield, current_row, current_column, "sink", all_ship_squares, ship_name)
                print_field(myfield)
            else:
                print("You have a hit!") 
                update_field(myfield, current_row, current_column, "hit")
                print_field(myfield)
        except(ValueError, IndexError):
            print("Oops! That's not a valid input. Please try again...")
        if not battleships.are_unsunk_ships_left(current_fleet): 
            game_over = True
            print(f"Great job! You required {shots} shots to sink the fleet.")

if __name__ == '__main__': 
   main()