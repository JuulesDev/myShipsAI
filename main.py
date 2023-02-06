from pprint import pprint
from random import randint
from batailleNavale import *

"""
    98% of the content of this file is for test purposes!
"""


def ships_to_ascii(ships: List[BNShip]) -> str:
    """Creates a ~beautiful~ ASCII grid from the ship list.

    Args:
        ships (List[BNShip]): The ships on the grid.

    Returns:
        str: The ASCII drawing.
    """
    grid = [["." for _ in range(BOARD_LENGTH)] for _ in range(BOARD_LENGTH)]
    for ship in ships:
        for cell in ship.get_cells():
            grid[cell[1]][cell[0]] = "X"
    return "\n".join(["".join(line) for line in grid])


def print_board(game: BatailleNavale) -> None:
    board = game.players[-game.turn].get_discovered_board()
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
    game = BatailleNavale()

    while True:
        if game.turn == 1:
            print_board(game)

            pos = input("Player 1: ").split(" ")

            if len(pos) != 2:
                continue

            try:
                pos = list(map(int, pos))
            except:
                continue

            if not game.play(pos[0], pos[1]):
                print("! TRY AGAIN !")
        else:
            game.play(randint(0, 10), randint(0, 10))
