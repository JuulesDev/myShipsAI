from typing import *
import random as rd

from .ship import BNShip, BNShipOrientation

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


def random_ship_pos(board_length: int, ship_length: int) -> BNShip:
    """Gives a random position and orientation to a ship with a give length.

    Args:
        length (int): The length of the ship.

    Returns:
        BNShip: The ship created.
    """
    x = rd.randint(0, board_length - ship_length)
    y = rd.randint(0, board_length - ship_length)
    ori = rd.choice(list(BNShipOrientation))
    return BNShip(x, y, ship_length, ori)


def create_random_ships_grid(board_length: int, ship_sizes: List[int]) -> List[BNShip]:
    """Creates possible boards with random ship positions.

    Returns:
        List[BNShip]: A list with the ship positions.
    """
    ships = []
    for ship_size in ship_sizes:
        # Looks for a possible place for each size of ship, and adds it to the result
        while True:
            ship = random_ship_pos(board_length, ship_size)
            if not check_ships_overlap(ships + [ship]):
                break
        ships.append(ship)
    return ships