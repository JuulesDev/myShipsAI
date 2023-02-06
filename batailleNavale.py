from typing import *
from enum import Enum
import random as rd

BOARD_LENGTH = 10
SHIP_SIZES = [
    5, 4, 3, 3, 2
]

# - Classes

class BNShipOrientation(Enum):
    """Represents the orientation that can have a BNShip.
    
    (The values assigned to both are the vectors that give us all the cells of a ship from the first one)
    """
    HORIZONTAL = (1, 0)
    VERTICAL = (0, 1)


class BNShip:
    """Represents a ship of the Bataille Navale.
    """
    def __init__(self, x: int, y: int, length: int, orientation: BNShipOrientation) -> None:
        # The x and y coordinates always refer to the most top left 'cell' of the ship. 
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation

    def __repr__(self) -> str:
        # Used for debug purposes
        return f"BNShip<x: {self.x}, y: {self.y}, len: {self.length}, ori: {self.orientation.name}>"


class BNPlayer:
    """Represents a player of the Bataille Navale.
    """
    def __init__(self) -> None:
        self.sightGrid = []
        self.boatGrid = []


class BatailleNavale:
    """Represents a game of Bataille Navale.
    """
    def __init__(self) -> None:
        self.players = {
            1: BNPlayer(),
            -1: BNPlayer()
        }
        self.turn = 1


# - Utils


def check_ships_overlap(ships: List[BNShip]) -> bool:
    """Tells if a list of ships overlap or not.

    Args:
        ships (List[BNShip]): The ships to check if they overlap.

    Returns:
        bool: True if they overlap, False otherwise.
    """
    already_used_cells = set()
    for ship in ships:
        for i_cell in range(ship.length):
            cell_x = ship.x + i_cell * ship.orientation.value[0]
            cell_y = ship.y + i_cell * ship.orientation.value[1]
            if (cell_x, cell_y) in already_used_cells:
                return True
            else:
                already_used_cells.add((cell_x, cell_y))
    return False


def random_ship_pos(length: int) -> BNShip:
    """Gives a random position and orientation to a ship with a give length.

    Args:
        length (int): The length of the ship.

    Returns:
        BNShip: The ship created.
    """
    x, y = rd.randint(0, BOARD_LENGTH - length), rd.randint(0, BOARD_LENGTH - length)
    ori = rd.choice(list(BNShipOrientation))
    return BNShip(x, y, length, ori)


def create_random_ships_grid() -> List[BNShip]:
    """Creates possible boards with random ship positions.

    Returns:
        List[BNShip]: A list with the ship positions.
    """
    ships = []
    for size in SHIP_SIZES: 
        # Looks for a possible place for each size of ship, and adds it to the result
        while True:
            ship = random_ship_pos(size)
            if not check_ships_overlap(ships + [ship]):
                break
        ships.append(ship)
    return ships