from cell import Cell
from a_star import a_star_search, print_labyrinth, labyrinth
import numpy as np
import image_process as img

def main():
    """Main Function"""

    start_cell = Cell(position=(165, 20))

    goal_cell = Cell(position=(25, 360))

    print()

    path = a_star_search(start_cell, goal_cell)
    
    print()

    assert path is not None
    _labyrinth = labyrinth.copy().astype(np.uint8)
    for _cell in path:
        # print(_cell)
        _labyrinth[_cell.row][_cell.column] = 5

    if path != []:
        _labyrinth[goal_cell.row][goal_cell.column] = 5

    for row in range(_labyrinth.shape[0]):
        for column in range(_labyrinth.shape[1]):
            if _labyrinth[row][column] == 5:
                _labyrinth[row][column] = 127

    # print_labyrinth(labyrinth)
    img.display("Laberinto :D", _labyrinth)

if __name__ == "__main__":
    main()