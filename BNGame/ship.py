from enum import Enum
from typing import *


class BNShipOrientation(Enum):
    """Represents the orientation that can have a BNShip.

    (The values assigned to both are the vectors that give us all the cells of a ship from the first one)
    """
    HORIZONTAL = (1, 0)
    VERTICAL = (0, 1)


class BNShip:
    """Represents a ship of the Bataille Navale.
    """

    def __init__(
        self, x: int, y: int, length: int, orientation: BNShipOrientation
    ) -> None:
        # The x and y coordinates always refer to the most top left 'cell' of the ship.
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation

    def __repr__(self) -> str:
        # Used for debug purposes
        return f"BNShip<x: {self.x}, y: {self.y}, len: {self.length}, ori: {self.orientation.name}>"

    def get_cells(self) -> List[Tuple[int, int]]:
        """Computes the position of each cell of the ship.

        Returns:
            List(Tuple(int, int)): The list of the cell positions [(x1, y1), (x2, y2), ...].
        """
        res = []
        for i_cell in range(self.length):
            cell_x = self.x + i_cell * self.orientation.value[0]
            cell_y = self.y + i_cell * self.orientation.value[1]
            res.append((cell_x, cell_y))
        return res
