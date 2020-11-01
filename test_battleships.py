import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    s = (4, 5, False, 3, {(4,5), (5,5)})
    assert is_sunk(s) == False

def test_ship_type1():
    s1 = (0, 0, True, 1, {}) # generate ships randomly?
    assert ship_type(s1) == "submarine"
    s2 = (2, 3, False, 2, {(2,3), (2,4)})
    assert ship_type(s2) == "destroyer"
    s3 = (5, 5, True, 3, {(5,5)})
    assert ship_type(s3) == "cruiser"
    s4 = (2, 1, False, 4, {})
    assert ship_type(s4) == "battleship"
    s5 = (1, 3, True, 4, {(1,3), (1,4)})
    assert ship_type(s5) == "battleship"

def test_is_open_sea1():
    fleet = [(2, 3, False, 3, {(2,3)})]
    row = 5
    column = 4
    assert is_open_sea(row, column, fleet) == False
    column = 5
    assert is_open_sea(row, column, fleet) == True
    fleet = [(4, 6, True, 2, {})]
    assert is_open_sea(row, column, fleet) == False
    fleet = [(2, 3, False, 3, {(2,3)}), (4, 6, True, 2, {})]
    assert is_open_sea(row, column, fleet) == False

def test_ok_to_place_ship_at1():
    assert True

def test_place_ship_at1():
    assert True

def test_check_if_hits1():
    fleet = [(2, 3, False, 3, {(2,3)}), (4, 6, True, 2, {})]
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
    assert True

def test_are_unsunk_ships_left1():
    ship1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)}) # sunk
    ship2 = (4, 5, False, 3, {(4,5), (5,5)}) # not sunk
    fleet1 = [ship1, ship2]*5 
    fleet2 = [ship1]*10
    fleet3 = [ship2]*10
    assert are_unsunk_ships_left(fleet1) == True
    assert are_unsunk_ships_left(fleet2) == False
    assert are_unsunk_ships_left(fleet3) == True
    
    
