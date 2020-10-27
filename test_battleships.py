import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    s = (2, 3, False, 3, {(2,3), (3,3)})
    assert is_sunk(s) == False

def test_ship_type1():
    s1 = (2, 3, False, 1, {})
    assert ship_type(s1) == "submarine"
    s2 = (2, 3, False, 2, {})
    assert ship_type(s2) == "destroyer"
    s3 = (2, 3, False, 3, {})
    assert ship_type(s3) == "cruiser"
    s4 = (2, 3, False, 4, {})
    assert ship_type(s4) == "battleship"

def test_is_open_sea1():
    assert True

def test_ok_to_place_ship_at1():
    assert True

def test_place_ship_at1():
    assert True

def test_check_if_hits1():
    assert True

def test_hit1():
    assert True

def test_are_unsunk_ships_left1():
    assert True
    
