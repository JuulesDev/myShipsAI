from pprint import pprint
import time
from typing import *
from random import randint
from BNGame import *

from BN_AIs import *

"""
    98% of the content of this file is for test purposes!
"""


# def ships_to_ascii(ships: List[BNShip]) -> str:
#     """Creates a ~beautiful~ ASCII grid from the ship list.

#     Args:
#         ships (List[BNShip]): The ships on the grid.

#     Returns:
#         str: The ASCII drawing.
#     """
#     grid = [["." for _ in range(10)] for _ in range(10)]
#     for ship in ships:
#         for cell in ship.get_cells():
#             grid[cell[1]][cell[0]] = "X"
#     return "\n".join(["".join(line) for line in grid])


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
            move = random_AI(game.get_discovered_board())
        else:
            move = random_AI(game.get_discovered_board())

        game.play(move)
        time.sleep(.5)
