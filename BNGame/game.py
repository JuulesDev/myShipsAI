from typing import *
from enum import Enum

from .utils import create_random_ships_grid
from .player import BNPlayer

class BNCellStatus(Enum):
    """Represents the status of a cell from a player perspective.
    """
    HIDDEN = 0
    MISSED = 1
    HIT = 2
    SUNK = 3
 

class BNGame:
    """Represents a game of Bataille Navale.
    """

    def __init__(self, board_length: int=10, ships_sizes: List[int]=[5, 4, 3, 3, 2]) -> None:
        self.board_length = board_length
        self.ship_sizes = ships_sizes
        self.players = {
            1: BNPlayer(create_random_ships_grid(self.board_length, self.ship_sizes)),
            -1: BNPlayer(create_random_ships_grid(self.board_length, self.ship_sizes)),
        }
        self.turn = 1

    def play(self, x: int, y: int) -> bool:
        """Makes the right player shoot somewhere on the board.

        Args:
            x (int): The x coordinate of the shoot.
            y (int): The y coordinate of the shoot.

        Returns:
            bool: True if everything went well, False otherwise.
        """
        if not (0 <= x < self.board_length and 0 <= y < self.board_length):
            return False  # Shot out of the board
        if (x, y) in self.players[-self.turn].discovered_cells:
            return False  # Already shot there
        self.players[-self.turn].discovered_cells.add((x, y))
        self.players[-self.turn].update_ships_sunk()

        if not (x, y) in self.players[-self.turn].ships_cells:
            self.turn = -self.turn  # Next player if missed
        return True
    
    def get_discovered_board(self) -> List[List[BNCellStatus]]:
        player = self.players[-self.turn]
        res = [
            [BNCellStatus.HIDDEN for _ in range(self.board_length)]
            for _ in range(self.board_length)
        ]
        for discovered_pos in player.discovered_cells:
            if discovered_pos in player.ships_cells:
                if discovered_pos in player.ships_sunk_cells:
                    res[discovered_pos[1]][discovered_pos[0]] = BNCellStatus.SUNK
                else:
                    res[discovered_pos[1]][discovered_pos[0]] = BNCellStatus.HIT
            else:
                res[discovered_pos[1]][discovered_pos[0]] = BNCellStatus.MISSED
        return res
