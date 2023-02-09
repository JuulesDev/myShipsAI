# PyBoat - Battleship
*Started on the February 6th 2023 by Jules (me, hi).*

## Description
Just an implementation of the 'Battleship' board game, the rules can be found [here on Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)). I also added few AIs that i tried using to play against myself. 

(I use 'BN' as an abbreviation of 'Battleship' because the french name of this game is 'La Bataille Navale'. Yes i mixed english and french, that's bad. Don't do that.)

## Project Files
In the `./BNGame` folder, there are all the files that make the game works. If you want to use it for yourself, you can import it and use it just as shown in the `./main.py` file.

In the `./BN_AIs` folder, there are the files of the AIs (pretty straightforward). Each AI has its own file, with the same-looking function that takes the state of the board as an input and outputs the position where it wants to shoot.

## Usage
- ### To add your own AI :
Simply add a file into `./BN_AIs`, add the basic function inside (you can copy it from another AI) and an import to your file into `./BN_AIs/__init__.py`. Then you'll be able to use it inside of the `./main.py` to make it compete against mines!
- ### To change the AIs that compete against each others :
Change the function that are inside the `AIs_used` list, putting more than 2 is useless. To see the avalaible AIs, take a look inside `./BN_AIs/__init__.py`.

## Todo
- [ ] Change the way to pick the AIs, make it more clear and easily usable.
- [ ] Add moooooore AIs.
- [ ] Add the ability to decide where our ships are (it's random for now).