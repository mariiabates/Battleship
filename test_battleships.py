#pylint: skip-file
import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    s = (4, 5, False, 3, {(4,5), (5,5)})
    assert is_sunk(s) == False 
    s = (4, 7, True, 2, set())
    assert is_sunk(s) == False

def test_ship_type1():
    s = (0, 0, True, 1, set()) # generate ships randomly?
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
    fleet = [(2, 3, False, 3, {(2,3)}), (4, 6, True, 2, {})]
    assert is_open_sea(row, column, fleet) == False
    fleet = [(4, 6, True, 2, set())]
    column = 4
    row = 4 
    assert is_open_sea(row, column, fleet) == True
    row = 5
    assert is_open_sea(row, column, fleet) == True

def test_ok_to_place_ship_at1():
    # Test horizontal ship with vertical 
    fleet = [(3, 3, False, 3, {(2,3)}), (4, 6, True, 2, set())] 
    row = 2
    column = 1
    horizontal = True
    length = 3
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    length = 2
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    length = 1
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

    row = 6 # lower bound
    length = 3
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    length = 2
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    length = 1
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

    row = 1 # upper bound
    column = 1
    horizontal = True
    length = 3
    fleet = [(3, 3, False, 3, {(2,3)}), (4, 6, True, 2, set())] 
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    length = 2
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    length = 1
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

    row = 7 # lower bound
    column = 1
    horizontal = True
    length = 3
    fleet = [(3, 3, False, 3, {(2,3)}), (4, 6, True, 2, set())] 
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    length = 2
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    length = 1
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at2():
    # Test vertical ship with vertical
    fleet = [(3, 3, False, 3, {(2,3)}), (4, 6, True, 2, set())] 
    row = 1 # upper bound
    column = 3
    horizontal = False
    length = 2
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    length = 1
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    row = 6 # lower bound
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    row = 7
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at3():
    # Test horizontal ship with horizontal
    fleet = [(4, 6, True, 2, set())]
    column = 6
    horizontal = True
    length = 3
    # Test upper and lower bound
    for row in {2, 6}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    for row in {3, 5}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    row = 5 
    column = 2 # left bound
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    column = 3
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    column = 8 # right bound
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    column = 9 
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at4():
    # Test vertical ship with horizontal
    fleet = [(4, 6, True, 2, set())]
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
    for column in {4, 9}:
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    for column in {5, 7}: 
        assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False
    

def test_place_ship_at1():
    fleet = []
    row = 2 
    column = 3 
    horizontal = False
    length = 3
    assert place_ship_at(row, column, horizontal, length, fleet) == [(2, 3, False, 3, set())]
    fleet = [(2, 3, False, 3, set())]
    row = 4
    column = 6
    horizontal = True
    length = 2
    assert place_ship_at(row, column, horizontal, length, fleet) == [(2, 3, False, 3, set()), (4, 6, True, 2, set())]

def test_check_if_hits1():
    # If hit same twice?
    fleet = [(2, 3, False, 3, {(2,3)}), (4, 6, True, 2, set())]
    # Tests for the 1st ship (vertical)
    row = 4
    column = 2
    assert check_if_hits(row, column, fleet) == False
    column = 3
    assert check_if_hits(row, column, fleet) == True
    row = 5
    assert check_if_hits(row, column, fleet) == False
    row = 1
    column = 3
    assert check_if_hits(row, column, fleet) == False
    # Tests for the 2nd ship (horizontal)
    row = 4
    column = 5
    assert check_if_hits(row, column, fleet) == False
    column = 7
    assert check_if_hits(row, column, fleet) == True
    row = 3
    assert check_if_hits(row, column, fleet) == False

def test_hit1():
    # Check return values
    fleet = [(2, 3, False, 3, set()), (4, 6, True, 2, set())]
    row = 4
    column = 3
    assert hit(row, column, fleet) == ([(2, 3, False, 3, {(4, 3)}), (4, 6, True, 2, set())], (2, 3, False, 3, {(4, 3)}))
    row = 3
    fleet = [(4, 6, True, 2, set()), (2, 3, False, 3, {(4, 3)})]
    assert hit(row, column, fleet) == ([(4, 6, True, 2, set()), (2, 3, False, 3, {(4, 3), (3, 3)})], (2, 3, False, 3, {(4, 3), (3, 3)}))


def test_are_unsunk_ships_left1():
    ship1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)}) # sunk
    ship2 = (4, 5, False, 3, {(4,5), (5,5)}) # not sunk
    fleet1 = [ship1, ship2]*5 
    fleet2 = [ship1]*10
    fleet3 = [ship2]*10
    assert are_unsunk_ships_left(fleet1) == True
    assert are_unsunk_ships_left(fleet2) == False
    assert are_unsunk_ships_left(fleet3) == True
    
    
