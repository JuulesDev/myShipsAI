from typing import *
from .ship import BNShip


class BNPlayer:
    """Represents a player of the Bataille Navale.
    """

    def __init__(self, ships: List[BNShip]) -> None:
        self.discovered_cells = set()
        self.ships_list = ships
        self.ships_cells = set()
        for ship in self.ships_list:
            for cell in ship.get_cells():
                self.ships_cells.add(cell)
        self.ships_sunk = []
        self.ships_sunk_cells = set()

    def update_ships_sunk(self) -> None:
        """Update the list of sunk ships.
        """
        self.ships_sunk = []
        for ship in self.ships_list:
            for cell in ship.get_cells():
                if not cell in self.discovered_cells:
                    break
            else:
                self.ships_sunk.append(ship)
        self.ships_sunk_cells = set()
        for ship in self.ships_sunk:
            for cell in ship.get_cells():
                self.ships_sunk_cells.add(cell)
