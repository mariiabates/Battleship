#see the readme.md file for description and data 


def is_sunk(ship):
    """Check if the ship is sunk.
    Return a Boolean value.
    """
    hits = ship[4]
    ship_length = ship[3]
    return len(hits) == ship_length

def ship_type(ship):
    """Check the ship type.
    Return a string ("battleship", "cruiser", "destroyer", or "submarine").
    """
    if ship[3] == 1:
        return "submarine"
    elif ship[3] == 2:
        return "destroyer"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 4:
        return "battleship"
    else:
        return "ship not found" # I don't need it?

def is_open_sea(row, column, fleet):
    """Check if the square given by row and column neither contains
    nor is adjacent to some ship in the fleet. 
    Return a Boolean value.
    """
    for ship in fleet:
        horizontal = ship[2]
        ship_row = ship[0]
        ship_col = ship[1]
        ship_len = ship[3]
        if not horizontal and abs(ship_row - row) <= ship_len and abs(ship_col - column) <= 1:
            return False
        if horizontal and abs(ship_row - row) <= 1 and abs(ship_col - column) <= ship_len:
            return False
    return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """Check if addition of a ship to the fleet (specified by row, column, horizontal, and length) 
    results in a legal arrangement. 
    Return a Boolean value.
    """
    def bad_cells_across(cell):
        """Helper function to return prohibited rows or columns, depending on what changes when we move across the ship"""
        return [cell + i for i in range(-1, +1 + 1)]
    def bad_cells_along(cell, ship_length):
        """Helper function to return prohibited rows or columns, depending on what changes when we move along the ship"""
        return [cell + i for i in range(-1, ship_length + 1)]

    # Create a set of cells that can't be occupied by the ship
    cells_bad = set()
    for ship in fleet:
        if ship[2]: # if horizontal
            rows_bad = bad_cells_across(ship[0]) 
            cols_bad = bad_cells_along(ship[1], ship[3]) 
        else: # if vertical
            rows_bad = bad_cells_along(ship[0], ship[3]) 
            cols_bad = bad_cells_across(ship[1])
        for r in rows_bad:
            for c in cols_bad:
                cells_bad.add((r,c)) 
                
    Create a set of cells occupied by the ship
    if horizontal:
        cells_target = {(row, column + i) for i in range(length)}
    else:
        cells_target = {(row + i, column) for i in range(length)}

    return len(cells_target & cells_bad) == 0

def place_ship_at(row, column, horizontal, length, fleet):
    """Add a ship, specified by row, column, horizontal, and length to the fleet.
    Return a new fleet.
    """
    fleet.append((row, column, horizontal, length, {}))
    return fleet # Can I modify?

def randomly_place_all_ships():
    """Make a random legal arrangement of 10 ships in the ocean. 
    This function makes use of the functions ok_to_place_ship_at and place_ship_at.
    Return a fleet.
    """
    # while length(fleet)!=10:
        # if ok_to_place_ship_at(): 
            # call place_ship_at()
    pass

# def check_if_hits(row, column, fleet):
#     """Check if the shot of the human player at the square represented by row and column
#     hits any of the ships of the fleet.
#     Return a Boolean value.
#     """
    

# def return index of ship was hit:
#     for ship in fleet:
#         horizontal = ship[2]
#         ship_row = ship[0]
#         ship_col = ship[1]
#         ship_len = ship[3]
#         # hitting vertical ships
#         if not horizontal and 0 <= (row - ship_row) < ship_len and ship_col == column:
#             #call hit
#             return True
#         # hitting horizontal ships
#         elif horizontal and ship_row == row and 0 <= (column - ship_col) < ship_len:
#             #call hit
#             return True # index 
#     return False

        
def hit(row, column, fleet): # + index
    """Perform a hit in the fleet at the square represented by row and column. 
    Return a tuple (fleet1, ship) where ship is the ship from the fleet and fleet1 is the fleet resulting from this hit.
    """
    # for ship in fleet:
    #     if ship[0]
    # result = (,)
    # for ship in fleet:
    # fleet = [(2, 3, False, 3, {}), (4, 6, True, 2, {})]
    # row = 4
    # column = 3
    # ([(2, 3, False, 3, {(4, 3)}), (4, 6, True, 2, {})], (2, 3, False, 3, {}))

def are_unsunk_ships_left(fleet):
    """Check if there are ships in the fleet that are still not sunk.
    Return a Boolean value.
    """
    #if every ship in fleet is_sunk:
        #return False
    #else:
        #return True
    result = False
    for ship in fleet:
        if not is_sunk(ship):
            result = True
    return result

# def main():
#     """Prompt the user to call out rows and columns of shots 
#     and outputs the responses of the computer iteratively until the game stops.
#     (a) there must be an option for the human player to quit the game at any time, 
#     (b) the program must never crash (i.e., no termination with Python error messages), whatever the human player does.
#     Returns nothing.
#     """
#     current_fleet = randomly_place_all_ships()

#     game_over = False
#     shots = 0

#     while not game_over:
#         loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
#         current_row = int(loc_str[0])
#         current_column = int(loc_str[1])
#         shots += 1
#         if check_if_hits(current_row, current_column, current_fleet):
#             print("You have a hit!")
#             (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
#             if is_sunk(ship_hit):
#                 print("You sank a " + ship_type(ship_hit) + "!")
#         else:
#             print("You missed!")

#         if not are_unsunk_ships_left(current_fleet): game_over = True

#     print("Game over! You required", shots, "shots.")


# if __name__ == '__main__': #keep this in
#    main()
