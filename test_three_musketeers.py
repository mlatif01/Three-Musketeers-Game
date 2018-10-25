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

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A0') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

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
        is_legal_move_by_musketeer(R, left)
    assert is_legal_move_by_musketeer((1,3),left) == True
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy(M, right)
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
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,2)) == [left, right, up]

def test_is_legal_location():
    set_board(board1)
    assert is_legal_location((2,2)) == True

def test_is_within_board():
    set_board(board1)
    assert is_within_board((3,1),left) == True

def test_all_possible_moves_for():
    set_board(board1)
    assert all_possible_moves_for(M) == [((1,3),left), ((2,2),left,right)]

def test_make_move():
    set_board(board1)
    assert make_move((2,2),left) == (2,1)
    
def test_choose_computer_move():
    set_board(board1)
    assert choose_computer_move(R) == ((3,1), left)

def test_is_enemy_win():
    set_board(board1)
    assert is_enemy_win() == False

