from typing import *

from BNGame import BNCellStatus


def user_input(board: List[List[BNCellStatus]]) -> Tuple[int, int]:
    pos = input("Select a move: ").split(" ")
    if len(pos) != 2:
        return -1 - 1
    try:
        pos = tuple(map(int, pos))
    except:
        return -1 - 1
    return pos
