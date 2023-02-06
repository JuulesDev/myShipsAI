from pprint import pprint
from batailleNavale import *

'''
    98% of the content of this file is for test purposes!
'''


def ships_to_ascii(ships: List[BNShip]) -> str:
    """Creates a ~beautiful~ ASCII grid from the ship list.

    Args:
        ships (List[BNShip]): The ships on the grid.

    Returns:
        str: The ASCII drawing.
    """
    grid = [['.' for _ in range(BOARD_LENGTH)] for _ in range(BOARD_LENGTH)]
    for ship in ships:
        for cell in ship.get_cells():
            grid[cell[1]][cell[0]] = 'X'
    return '\n'.join([''.join(line) for line in grid])


if __name__ == '__main__':
    game = BatailleNavale()

    while True:
        board = game.players[-game.turn].get_discovered_board()
        txt_board = ''
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == BNCellStatus.HIDDEN:
                    txt_board += '.'
                elif board[y][x] == BNCellStatus.MISSED:
                    txt_board += 'O'
                else:
                    txt_board += 'X'
            txt_board += '\n'
        print(txt_board)

        player = 1 if game.turn == 1 else 2
        pos = input('Player {player}: ').split(' ')

        if len(pos) != 2:
            continue
        
        try:
            pos = list(map(int, pos))
        except:
            continue

        if not game.play(pos[0], pos[1]):
            print('! TRY AGAIN !')
