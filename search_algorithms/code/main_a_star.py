from cell import Cell
from a_star import a_star_search, print_labyrinth, labyrinth
import numpy as np
import image_process as img

OFFSET = 10
file = open('coordenadas.txt', 'w')

def main():
    """Main Function"""

    start_cell = Cell(position=(165, 20)) # 63, 12

    goal_cell = Cell(position=(25, 360)) # 8, 134

    print()

    path = a_star_search(start_cell, goal_cell)
    
    print()

    assert path is not None
    _labyrinth = labyrinth.copy().astype(np.uint8)
    for index in range(0, len(path), 20):
        _cell = path[index]
        #print(_cell)
        if _labyrinth[_cell.row - 1][_cell.column + 8] == 0 or _labyrinth[_cell.row - 1][_cell.column - 8] == 0:
            _cell.row += OFFSET
        if _labyrinth[_cell.row + 1][_cell.column + 8] == 0 or _labyrinth[_cell.row + 1][_cell.column - 8] == 0:
            _cell.row -= OFFSET

        # es el de arriba un obstaculo?
        if _labyrinth[_cell.row - 1][_cell.column] == 0:
            _cell.row += OFFSET
        # es el de abajo un obstaculo?
        if _labyrinth[_cell.row + 1][_cell.column] == 0:
            _cell.row -= OFFSET
        # es el de la izquierda un obstaculo?
        if _labyrinth[_cell.row][_cell.column - 1] == 0:
            _cell.column += OFFSET
        # es el de la derecha un obstaculo?
        if _labyrinth[_cell.row][_cell.column + 1] == 0:
            _cell.column -= OFFSET
        _labyrinth[_cell.row][_cell.column] = 127

        print(_cell, file=file)

    if path != []:
        _labyrinth[goal_cell.row][goal_cell.column] = 127

    file.close()
    # print_labyrinth(labyrinth)
    img.display("Laberinto :D", _labyrinth)

if __name__ == "__main__":
    main()