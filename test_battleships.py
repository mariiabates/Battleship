#pylint: skip-file
import pytest
from battleships import *

def test_is_sunk():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    s = (4, 5, False, 3, {(4,5), (5,5)})
    assert is_sunk(s) == False
    s = (4, 7, True, 2, set())
    assert is_sunk(s) == False
    s = (5, 5, True, 3, {(5,5)})
    assert is_sunk(s) == False
    s = (5, 5, True, 3, {(5,5), (5,6), (5,7)})
    assert is_sunk(s) == True

def test_ship_type():
    s = (0, 0, True, 1, set())
    assert ship_type(s) == "submarine"
    s = (2, 3, False, 2, {(2,3), (2,4)})
    assert ship_type(s) == "destroyer"
    s = (5, 5, True, 3, {(5,5)})
    assert ship_type(s) == "cruiser"
    s = (2, 1, False, 4, set())
    assert ship_type(s) == "battleship"
    s = (1, 3, True, 4, {(1,3), (1,4)})
    assert ship_type(s) == "battleship"

def test_is_open_sea1():
    fleet = [(2, 3, False, 3, {(2,3)})]
    row = 5
    column = 4
    assert is_open_sea(row, column, fleet) == False
    column = 5
    assert is_open_sea(row, column, fleet) == True
    fleet = [(4, 6, True, 2, set())]
    assert is_open_sea(row, column, fleet) == False
    column = 4
    row = 4 
    assert is_open_sea(row, column, fleet) == True
    row = 5
    assert is_open_sea(row, column, fleet) == True
    fleet = [(2, 3, False, 3, {(2,3)}), (4, 6, True, 2, {})]
    assert is_open_sea(row, column, fleet) == False    

def test_ok_to_place_ship_at1():
    """Test placing a horizontal ship with a vertical ship.""" 
    fleet = [(3, 3, False, 3, set()), (4, 6, True, 2, set())] 
    column = 1
    horizontal = True
    for row in {2, 6}:
        length = 3
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
        length = 2
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
        length = 1
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    for row in {1, 7}:
        length = 3
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
        length = 2
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
        length = 1
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at2():
    """Test placing a vertical ship with another vertical one."""
    fleet = [(3, 3, False, 3, set()), (4, 6, True, 2, set())] 
    horizontal = False
    length = 2
    column = 3
    row = 1 # upper bound
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    length = 1
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    row = 6 # lower bound
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    row = 7
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at3():
    """Test placing a horizontal ship with another horizontal one."""
    fleet = [(4, 4, True, 2, set())]
    horizontal = True
    length = 3
    # Test upper and lower bound
    column = 4
    for row in {2, 6}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    for row in {3, 5}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    # Test left and right bound
    row = 4
    for column in {1, 6}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    for column in {0, 7}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at4():
    """Test placing a vertical ship with a horizontal ship."""
    fleet = [(4, 5, True, 2, set())]
    horizontal = False
    length = 2
    # Test upper and lower bound
    column = 6
    for row in {2, 5}: 
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    for row in {1, 6}: 
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    # Test left and right bound
    row = 4
    for column in {3, 8}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    for column in {4, 7}: 
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False

def test_ok_to_place_ship_at5():
    """Check boundaries of the playing field."""
    fleet = []
    row = 9
    column = 9
    for horizontal in {True, False}:
        length = 1
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
        length = 2
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    assert ok_to_place_ship_at(5, 9, True, 3, [(4, 6, True, 2, set())]) == False

def test_place_ship_at():
    """N.B. Based on the implementation of the function, the fleet should be declared each time."""
    fleet = []
    assert place_ship_at(2, 3, False, 3, fleet) == [(2, 3, False, 3, set())]
    fleet = []
    assert place_ship_at(6, 5, True, 4, fleet) == [(6, 5, True, 4, set())]
    fleet = [(2, 3, False, 3, set())]
    assert place_ship_at(4, 6, True, 2, fleet) == [(2, 3, False, 3, set()), (4, 6, True, 2, set())]
    row = 9
    column = 9
    length = 1
    fleet = [(2, 3, False, 3, set()), (4, 6, True, 2, set())]
    horizontal = True
    assert place_ship_at(row, column, horizontal, length, fleet) == [(2, 3, False, 3, set()), (4, 6, True, 2, set()), (9, 9, True, 1, set())]
    fleet = [(2, 3, False, 3, set()), (4, 6, True, 2, set())]
    horizontal = False
    assert place_ship_at(row, column, horizontal, length, fleet) == [(2, 3, False, 3, set()), (4, 6, True, 2, set()), (9, 9, False, 1, set())]

# Full fleet as a global variable
fleet_seed_22 = [(2, 3, True, 4, {(2, 5)}), (4, 6, True, 3, set()), (4, 2, False, 3, set()), (6, 0, False, 2, {(6, 0)}), \
    (8, 6, False, 2, set()), (0, 3, True, 2, set()), (0, 8, False, 1, set()), (0, 1, True, 1, set()), (2, 9, False, 1, set()), (8, 2, False, 1, {(8, 2)})]

def test_check_if_hits():
    fleet = [(2, 3, False, 3, {(2,3)}), (4, 6, True, 2, set())]
    # Tests for the 1st ship (vertical)
    row = 4
    column = 3
    assert check_if_hits(row, column, fleet) == True
    row = 5
    assert check_if_hits(row, column, fleet) == False
    row = 1
    assert check_if_hits(row, column, fleet) == False
    column = 2
    assert check_if_hits(row, column, fleet) == False
    # Tests for the 2nd ship (horizontal)
    column = 5
    row = 4
    assert check_if_hits(row, column, fleet) == False
    column = 7
    assert check_if_hits(row, column, fleet) == True
    row = 3
    assert check_if_hits(row, column, fleet) == False
    # Tests for the full fleet
    assert check_if_hits(5, 5, fleet_seed_22) == False
    assert check_if_hits(7, 0, fleet_seed_22) == True

def test_hit():
    """N.B. Based on the implementation of the function, the fleet should be declared each time."""
    fleet = [(2, 3, False, 3, set()), (4, 6, True, 2, set())]
    column = 3
    row = 4
    assert hit(row, column, fleet) == ([(2, 3, False, 3, {(4, 3)}), (4, 6, True, 2, set())], (2, 3, False, 3, {(4, 3)}))
    fleet = [(2, 3, False, 3, {(4, 3)}), (4, 6, True, 2, set())]
    row = 3
    assert hit(row, column, fleet) == ([(2, 3, False, 3, {(4, 3), (3, 3)}), (4, 6, True, 2, set())], (2, 3, False, 3, {(4, 3), (3, 3)}))
    # Test a change of order of the ships in fleet
    fleet = [(4, 6, True, 2, set()), (2, 3, False, 3, {(4, 3)})] 
    assert hit(row, column, fleet) == ([(4, 6, True, 2, set()), (2, 3, False, 3, {(4, 3), (3, 3)})], (2, 3, False, 3, {(4, 3), (3, 3)}))
    fleet = [(4, 6, True, 2, set()), (2, 3, False, 3, {(4, 3), (3, 3)})] 
    assert hit(4, 6, fleet) == ([(4, 6, True, 2, {(4, 6)}), (2, 3, False, 3, {(4, 3), (3, 3)})], (4, 6, True, 2, {(4, 6)}))
    # Test the full fleet
    assert hit(7, 0, fleet_seed_22) == ([(2, 3, True, 4, {(2, 5)}), (4, 6, True, 3, set()), (4, 2, False, 3, set()), (6, 0, False, 2, {(7, 0), (6, 0)}), \
    (8, 6, False, 2, set()), (0, 3, True, 2, set()), (0, 8, False, 1, set()), (0, 1, True, 1, set()), (2, 9, False, 1, set()), (8, 2, False, 1, {(8, 2)})], (6, 0, False, 2, {(7, 0), (6, 0)}))

def test_are_unsunk_ships_left():
    ship1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)}) # sunk
    ship2 = (4, 5, False, 3, {(4,5), (5,5)}) # not sunk
    fleet1 = [ship1, ship2] * 5 
    fleet2 = [ship1] * 10
    fleet3 = [ship2] * 10
    fleet4 = [ship1] * 9 + [ship2]
    assert are_unsunk_ships_left(fleet1) == True
    assert are_unsunk_ships_left(fleet2) == False
    assert are_unsunk_ships_left(fleet3) == True
    assert are_unsunk_ships_left(fleet4) == True
    assert are_unsunk_ships_left(fleet_seed_22) == True
    fleet_sunk = [(2, 3, True, 4, {(2,5),(2,3),(2,4),(2,6)}), (4, 6, True, 3, {(4,6),(4,8),(4,7)}), (4, 2, False, 3, {(4,2),(5,2),(6,2)}), (6, 0, False, 2, {(6,0),(7,0)}), \
    (8, 6, False, 2, {(8,6),(9,6)}), (0, 3, True, 2, {(0,4),(0,3)}), (0, 8, False, 1, {(0,8)}), (0, 1, True, 1, {(0,1)}), (2, 9, False, 1, {(2,9)}), (8, 2, False, 1, {(8,2)})]
    assert are_unsunk_ships_left(fleet_sunk) == False