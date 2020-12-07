# tic tac toe created 01/12/2020, for practicing python
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
    # i can add all the winning coordinates here.
    if board[0] == logo and board[1] == logo and board[2] == logo:
        print(f'Wow.. {logo} --> Congrats you have won ... .. .')
        return True


def check_tie(board):
    if " " not in board:
        print(' Game Tie ... ... .')
        return False


def check_box_if_empty(player, logo, board):
    if board[player] == " ":
        board[player] = logo
    else:
        print(f'{ player } is not free')
        return True


def ask_player(player_logo):
    try:
        return int(input(f'Mr {player_logo} please enter number 0 - 8 ...'))
    except ValueError as ve:
        print(f'{ve}You are supposed to enter positive number.')


def play_again():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]



def play():

    box = board()
    
    # i can create a dynamic func for the player, but it is not a big deal ...
    while True:

        player_1 = ask_player("Player_1")
        check_box_if_empty(player_1, "X", box)
        board_printer(box)
        if check_winner("X", box):
            break

        if check_tie(box) == False:
            ask = input('Play again Y/N').upper()
            if ask == "Y":
                box = play_again()
                continue
            else:
                break


        # Second player
        player_2 = ask_player("player_2")
        check_box_if_empty(player_2, "0", box)
        board_printer(box)
        if check_winner("Y", box):
            break

        if check_tie(box) == False:
            ask = input('Play again Y/N').upper()
            if ask == "Y":
                box = play_again()
                continue
            else:
                break


play()