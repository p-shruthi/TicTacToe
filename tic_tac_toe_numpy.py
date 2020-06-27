import numpy as np
import random
def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

    def handle_turn():
        position = int(input())
        position=position-1
        if(position >=0 & position <= 9):
            if board[position] == "X" or board[position] == "O":
                print("\nYou can't go there. Try again")
                handle_turn()
            else:
                board[position] = "X"
        else:
            print("\nThat's not on the board. Try again")

    def check_random_turn():
        position = np.random.choice(9)
        if board[position] == "X" or board[position] == "O":
            print("\nYou can't go there. Try again")
            check_random_turn()
        else:
            board[position] = "O"

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 wins!!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not valid:
        draw()
        valid = check_board()
        if valid == True:
            break
        print("Player 1 choose where to place a cross")
        handle_turn()
        print()
        draw()
        valid = check_board()
        if valid == True:
            break
        print("Player 2 choose where to place a nought")
        check_random_turn()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()
tic_tac_toe()