def main():
    player_1_marker = input("Player 1, do you want to be 'X' or 'O'?\n")
    player_2_marker = ""
    if player_1_marker == "X":
        player_2_marker = "O"
    elif player_1_marker == "O":
        player_2_marker = "X"
    else:
        print("Not 'X' or 'O'. Please try again.")
        exit()

if __name__ == "__main__":
    main()
