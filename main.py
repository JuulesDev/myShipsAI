import time
from typing import *

from BNGame import *
from BN_AIs import *

"""
    98% of the content of this file is for test purposes!
"""
AIs_used = [
    random_AI,
    random_AI
]


def print_board(game: BNGame) -> None:
    board = game.get_discovered_board()
    txt_board = ""
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == BNCellStatus.HIT:
                txt_board += "X"
            elif board[y][x] == BNCellStatus.SUNK:
                txt_board += "$"
            elif board[y][x] == BNCellStatus.MISSED:
                txt_board += "O"
            else:
                txt_board += "."
        txt_board += "\n"
    print(txt_board)


if __name__ == "__main__":
    game = BNGame()

    while True:
        print(game.turn)
        print_board(game)

        move = None
        if game.turn == 1:
            move = AIs_used[0](game.get_discovered_board())
        else:
            move = AIs_used[1](game.get_discovered_board())

        game.play(move)
        time.sleep(.5)
