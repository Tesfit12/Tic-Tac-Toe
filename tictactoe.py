# tic tac toe created 01/12/2020, for practicing python
# modified code

def board():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return board


def board_printer(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-----')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-----')
    print(f'{board[6]}|{board[7]}|{board[8]}')


def check_winner(logo, board):
    if board[0] == logo and board[1] == logo and board[2] == logo or \
            board[3] == logo and board[4] == logo and board[5] == logo or \
            board[6] == logo and board[7] == logo and board[8] == logo or \
            board[0] == logo and board[3] == logo and board[6] == logo or \
            board[0] == logo and board[4] == logo and board[8] == logo or \
            board[6] == logo and board[4] == logo and board[2] == logo:
        print(f'Wow.. {logo} --> Congrats you have won ... .. .')
        return True


def check_tie(board):
    if " " not in board:
        print(' Game Tie ... ... .')
        return True


def check_box_if_empty(player, logo, board):
    try:
        if board[player] == " ":
            board[player] = logo
        else:
            print(f'{player} is not free')
            return True

    except IndexError as IX:
        print(f'You Should Enter numbers [ 0 - 8 ]---> {IX}')



def ask_player(player_logo):
    try:
        user_num = int(input(f'Mr {player_logo} please enter number [ 0 - 8 ]...'))
        return user_num

    except ValueError as ve:
        print(f'You are supposed to enter positive number. {ve}')
        return -1


def ask_to_play_again():
    ask = input('Play again Y/N').upper()
    if ask == "Y":
        return True
    else:
        return False


def start_game(player_input, logo, board):

    gamer = ask_player(player_input)

    if gamer == -1:
        return False
    else:
        check_box_if_empty(gamer, logo, board)
        board_printer(board)

        if check_winner(logo, board):
            return True




def play_again():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]



def main_func():
    box = board()

    while True:

        if start_game('player_1', "X", box):  # start the game
            if ask_to_play_again():  # ask him to play again
                box = play_again()   # reset the board
                continue
            else:
                break

        if check_tie(box):  # check if tie
            break


        if start_game('player_2', "0", box):
            if ask_to_play_again():
                box = play_again()
                continue
            else:
                break

        if check_tie(box):
            break





main_func()