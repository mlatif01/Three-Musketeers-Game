# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.
import random
import json


def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    M = 'M'
    R = 'R'
    _ = "-"
    board = [[R, R, R, R, M],
             [R, R, R, R, R],
             [R, R, M, R, R],
             [R, R, R, R, R],
             [M, R, R, R, R]]

left = 'left'
right = 'right'
up = 'up'
down = 'down'


def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board


def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board


def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    row_col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    if s[0] in row_col.keys() and 1 <= int(s[1]) <= 5 and s != None:
        return (row_col[s[0]], int(s[1]) - 1)
    else:
        raise ValueError("Input is outside of the correct range")


def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    col_row = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}
    if location[0] in col_row.keys() and 0 <= location[1] <= 4:
        return "{}{}".format(col_row[location[0]], location[1] + 1)
    else:
        raise ValueError("Input is outside of correct range")


def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    try:
        return board[location[0]][location[1]]
    # Bug fix
    except IndexError:
        pass


def all_locations():
    """Returns a list of all 25 locations on the board."""
    lis = []
    for i in range(5):
        for j in range(5):
            lis.append((i, j))
    return lis


def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, col) = location
    dic = {up: (-1, 0), down: (+1, 0), left: (0, -1), right: (0, +1)}
    return (row + dic[direction][0], col + dic[direction][1])


def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location) != "M":
        raise ValueError("Piece at location is not Musketeer")
    elif at(adjacent_location(location, direction)) == "R":
        return True
    else:
        return False


def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location) != "R":
        raise ValueError("Piece at location is not R")
    elif at(adjacent_location(location, direction)) == "-":
        return True
    else:
        return False


def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location) == "M":
        return is_legal_move_by_musketeer(location, direction)
    elif at(location) == "R":
        return is_legal_move_by_enemy(location, direction)


def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    directions = [up, down, left, right]
    if at(location) == "M":
        for i in range(len(directions)):
            if at(adjacent_location(location, directions[i])) == "R":
                return True
    elif at(location) == "R":
        for i in range(len(directions)):
            if at(adjacent_location(location, directions[i])) == "-":
                return True
    return False


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    dic = {}
    for i in range(5):
        for j in range(5):
            if at((i, j)) != "-":
                dic[(i, j)] = get_board()[i][j]
    for k, v in dic.items():
        if v == who:
            try:
                if can_move_piece_at(k):
                    return True
            except IndexError:
                print("{} at {} is checking a position out of range".format(v, k))
    return False


def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will be a pair of integer numbers."""
    if 0 <= location[0] <= 4 and 0 <= location[1] <= 4:
        return True
    return False


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    directions = ["up", "down", "left", "right"]
    moves = []
    for dir in directions:
        if is_legal_move(location, dir) and is_legal_location(adjacent_location(location, dir)):
            moves.append(dir)
    return moves


def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    next_location = adjacent_location(location, direction)
    if is_legal_location(next_location):
        return True
    return False


def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    all_possible_moves = []
    for loc in all_locations():
        if at(loc) == player and possible_moves_from(loc) != []:
            all_possible_moves.append((loc, possible_moves_from(loc)))
    if all_possible_moves != []:
        return all_possible_moves


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    adj_location = adjacent_location(location, direction)
    board[adj_location[0]][adj_location[1]] = board[location[0]][location[1]]
    board[location[0]][location[1]] = "-"


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    if all_possible_moves_for(who) != None:
        choices = all_possible_moves_for(who)
        choice = random.choice(choices)
        return (choice[0], random.choice(choice[1]))


def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    loc_of_m = []
    for piece in all_locations():
        if at(piece) == "M":
            loc_of_m.append(piece)
    check_row = [x[0] for x in loc_of_m]
    check_col = [x[1] for x in loc_of_m]
    return check_row.count(check_row[0]) == len(check_row) or check_col.count(check_col[0]) == len(check_col)

# ---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end=" ")
        for j in range(0, 5):
            print(board[i][j] + " ", end=" ")
        print()
        ch = chr(ord(ch) + 1)
    print()


def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.
""")
    print()


def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user


def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L': 'left', 'R': 'right', 'U': 'up', 'D': 'down'}
    move = input("Your move? ").upper().replace(' ', '')
    # Save game state
    if move == "S":
        save_game()
        get_users_move()
    elif (len(move) >= 3
          and move[0] in 'ABCDE'
          and move[1] in '12345'
          and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()


def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else:  # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)


def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else:  # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board


def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from', \
          location_to_string(location), 'to', \
          location_to_string(new_location) + ".\n")


def prompt_load_or_new():
    """ Asks user if they want to load previous game or start a new game"""
    inp = input("Type 'L' to load a previous game OR 'N' to start a new game: ").lower()
    return inp


def load_game():
    """Loads a previous game"""
    with open('prevgame.txt', 'r') as filehandle:
        prev_board = json.load(filehandle)
    set_board(prev_board)


def save_game():
    """Saves the current state of the game"""
    new_board = get_board()
    with open('prevgame.txt', 'w') as filehandle:
        json.dump(new_board, filehandle)
    print("The game has been saved")


def start_game():
    """Starts the Three Musketeers Game."""
    load_or_new = prompt_load_or_new()
    if load_or_new == "l":
        print("Loading previous board...")
        users_side = choose_users_side()
        load_game()
    elif load_or_new == "n":
        print("Starting new game! \n!!Type 'S' if you want to save the game state when choosing move!!")
        users_side = choose_users_side()
        board = create_board()
    print_instructions()
    print_board()
    main_game(users_side)


def main_game(users_side):
    """Plays the main game"""
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

#Uncomment below to start the game
start_game()