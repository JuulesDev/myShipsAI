from typing import *
from random import randint

from BNGame import BNCellStatus


def random_AI(board: List[List[BNCellStatus]]) -> Tuple[int, int]:
    return randint(0, 10), randint(0, 10)
