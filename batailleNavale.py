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

class BNCellStatus(Enum):
    """Represents the status of a cell from a player perspective.
    """
    HIDDEN = 0
    MISSED = 1
    HIT = 2


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


class BNPlayer:
    """Represents a player of the Bataille Navale.
    """
    def __init__(self, ships: List[BNShip]) -> None:
        self.discoveredGrid = set()
        self.shipsList = ships
        self.shipCellPos = set()
        for ship in self.shipsList:
            for cell in ship.get_cells():
                self.shipCellPos.add(cell)
        

    def get_discovered_board(self) -> List[List[BNCellStatus]]:
        res = [[BNCellStatus.HIDDEN for _ in range(BOARD_LENGTH)] for _ in range(BOARD_LENGTH)]
        for discovered_pos in self.discoveredGrid:
            if discovered_pos in self.shipCellPos:
                res[discovered_pos[1]][discovered_pos[0]] = BNCellStatus.HIT
            else:
                res[discovered_pos[1]][discovered_pos[0]] = BNCellStatus.MISSED
        return res


class BatailleNavale:
    """Represents a game of Bataille Navale.
    """
    def __init__(self) -> None:
        self.players = {
            1: BNPlayer(create_random_ships_grid()),
            -1: BNPlayer(create_random_ships_grid())
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
        if not (0 <= x < BOARD_LENGTH and 0 <= y < BOARD_LENGTH):
            return False # Shot out of the board
        if (x, y) in self.players[-self.turn].discoveredGrid:
            return False # Already shot there
        self.players[-self.turn].discoveredGrid.add((x, y))
        self.turn = -self.turn # Next player
        return True


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
        for cell in ship.get_cells():
            if cell in already_used_cells:
                return True
            else:
                already_used_cells.add(cell)
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

