board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_',]

game_still_going = True

winner = None

current_player = 'X'

def display_board():
    print()
    print('   ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_game():
    display_board()
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print()
        print('   ' + winner + ' is the winner.')
    elif winner == None:
        print()
        print('   Tie.')

def handle_turn(player):
    print()
    print('   ' + player + "'s turn ")
    print()
    position = input('   Select Your position: ')

    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print()
            print('   ' + player + "'s turn ")
            print()
            position = input('   Select Your position: ')

        position = int(position) - 1
        if board[position] == '_':
            valid = True
        else:
            print()
            print('   It is already filled up.')

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    global winner

    row_winner = check_rows()

    coloumn_winner = check_coloumns()

    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():

    global game_still_going
    row1 = board[0] == board[1] == board[2] !='_'
    row2 = board[3] == board[4] == board[5] !='_'
    row3 = board[6] == board[7] == board[8] !='_'

    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return

def check_coloumns():

    global game_still_going
    coloumn1 = board[0] == board[3] == board[6] !='_'
    coloumn2 = board[1] == board[4] == board[7] !='_'
    coloumn3 = board[2] == board[5] == board[8] !='_'

    if coloumn1 or coloumn2 or coloumn3:
        game_still_going = False
    if coloumn1:
        return board[0]
    if coloumn2:
        return board[1]
    if coloumn3:
        return board[2]
    return

def check_diagonals():

    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] !='_'
    diagonal2 = board[2] == board[4] == board[6] !='_'

    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if '_' not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

play_game()
