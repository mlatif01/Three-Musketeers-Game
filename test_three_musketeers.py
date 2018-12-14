import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, M, M, _, _],
            [M, _, _, R, _],
            [_, R, R, R, _],
            [_, R, _, _, _],
            [_, _, _, _, _] ]

board3 =  [ [_, _, _, _, _],
            [_, _, _, R, M],
            [M, R, R, R, _],
            [_, R, _, _, _],
            [_, _, M, _, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((4,0)) == M
    assert at((2,1)) == R

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    set_board(board2)
    assert at((0,1)) == M
    assert at((0,4)) == _
    assert at((1,3)) == R

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location("X3")
    with pytest.raises(ValueError):
        string_to_location("A7")
    assert string_to_location("A1") == (0,0)
    assert string_to_location("C3") == (2,2)
    assert string_to_location("E1") == (4,0)

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((6,3))
    assert location_to_string((0,4)) == "A5"

def test_at():
    set_board(board1)
    assert at((1,3)) == M
    assert at((0,0)) == _
    assert at((4,3)) == R

def test_all_locations():
    set_board(board1)
    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                               (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

def test_adjacent_location():
    set_board(board1)
    assert adjacent_location((2,2),left) == (2,1)
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((1, 2), left)
    assert is_legal_move_by_musketeer((1,3),left) == True
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((1, 3), right)
    assert is_legal_move_by_enemy((1,2),left) == True

def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((0,3),right) == False

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((2,2)) == True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,2)) == [up, left, right]

def test_is_legal_location():
    set_board(board1)
    assert is_legal_location((2,2)) == True

def test_is_within_board():
    set_board(board1)
    assert is_within_board((3,1),left) == True

def test_all_possible_moves_for():
    set_board(board1)
    assert all_possible_moves_for(M) == [((1,3),["down","left"]), ((2,2),["up","left","right"])]

def test_make_move():
    set_board(board1)
    assert make_move((2,2),left) == None
    
def test_choose_computer_move():
    set_board(board3)
    assert choose_computer_move(M) == ((2,0), "right") or ((1,4), "left")

def test_is_enemy_win():
    set_board(board1)
    assert is_enemy_win() == False


