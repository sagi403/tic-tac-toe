board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}


def reset_board():
    for n in range(1, 10):
        board[n] = " "


def build_board():

    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("     |     |     ")


def check_winner():
    if board[1] == board[2] == board[3] != " ":
        return True
    elif board[4] == board[5] == board[6] != " ":
        return True
    elif board[7] == board[8] == board[9] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[3] == board[6] == board[9] != " ":
        return True
    elif board[1] == board[5] == board[9] != " ":
        return True
    elif board[3] == board[5] == board[7] != " ":
        return True
    else:
        return False


def playing(player):
    global count
    build_board()
    next_turn = False
    while not next_turn:
        user = int(input(f"Please enter the number you wish to place '{player}' in his place: "))
        if board[user] == " ":
            board[user] = player
            next_turn = True
            check = check_winner()
            count += 1
            if check:
                build_board()
                return True
        else:
            print("You enter incorrect input.")


want_to_play = True
winner = False
count = 0
while want_to_play:
    print("Lets Play Tic-Tac-Toe!\n")
    while not winner:
        winner = playing("X")
        if winner:
            print("Player X is the winner!")
        elif count == 9:
            build_board()
            winner = True
            print("Draw!")
        else:
            winner = playing("O")
            if winner:
                print("Player O is the winner!")
            elif count == 9:
                build_board()
                winner = True
                print("Draw!")
    continue_playing = input("Do you want to play another game? Type 'Yes' / 'No': ").lower()
    if continue_playing == "yes":
        reset_board()
        winner = False
        count = 0
    else:
        want_to_play = False

print("Thank you for playing with us!")


