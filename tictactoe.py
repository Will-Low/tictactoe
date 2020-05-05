board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def main():
    start_game()

def start_game():
    global board
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    player_1_marker = input("Player 1, do you want to be 'X' or 'O'?\n").upper()
    player_2_marker = ""
    if player_1_marker == "X":
        player_2_marker = "O"
    elif player_1_marker == "O":
        player_2_marker = "X"
    else:
        print("Not 'X' or 'O'. Please try again.")
        start_game()

    while True:
        conduct_turn("Player 1", player_1_marker)
        conduct_turn("Player 2", player_2_marker)

def check_for_win(board, player_marker):
    if (board[0][0] == board[0][1] == board[0][2] == player_marker
        or board[1][0] == board[1][1] == board[1][2] == player_marker
        or board[2][0] == board[2][1] == board[2][2] == player_marker
        or board[0][0] == board[1][0] == board[2][0] == player_marker
        or board[0][1] == board[1][1] == board[2][1] == player_marker
        or board[0][2] == board[1][2] == board[2][2] == player_marker
        or board[0][0] == board[1][1] == board[2][2] == player_marker
        or board[0][2] == board[1][1] == board[2][0] == player_marker):
            play_again = input("You win! Play again? (y/n)").lower()
            if play_again == "y":
                start_game()
            elif play_again == "n":
                exit()
            else:
                print("Unrecognized. Quitting...")
                exit()

def print_board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def conduct_turn(player, player_marker):
    global board
    print_board(board)
    move_position = input("Your move, " + player + " (" + player_marker + "): ")
    place_marker(move_position, player_marker)
    check_for_win(board, player_marker)

def place_marker(move_position, player_marker):
    # Contains a security vulnerability
    if move_position == "1":
        board[0][0] = player_marker
    elif move_position == "2":
        board[0][1] = player_marker
    elif move_position == "3":
        board[0][2] = player_marker
    elif move_position == "4":
        board[1][0] = player_marker
    elif move_position == "5":
        board[1][1] = player_marker
    elif move_position == "6":
        board[1][2] = player_marker
    elif move_position == "7":
        board[2][0] = player_marker
    elif move_position == "8":
        board[2][1] = player_marker
    elif move_position == "9":
        board[2][2] = player_marker
    else:
        try_again_position = input("Not a valid position. Pick a valid position number: ")
        place_marker(try_again_position, player_marker)

if __name__ == "__main__":
    main()
