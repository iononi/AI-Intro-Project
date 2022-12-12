from cell import Cell
from collections import deque
import image_process as img

# inicialización
# carga la imagen
original_labyrith = img.load_image("img/borderless.png")
thick_labyrinth = img.load_image("img/thicker_borders.png")

# aquí obtenemos la imagen del laberinto binarizada (0/255)
labyrinth = img.binarize_image(original_labyrith)

ROWS = thick_labyrinth.shape[0] # la shape es (filas, columnas)
COLUMNS = thick_labyrinth.shape[1]

B = 0 # bloqueado
F = 255 # libre/desbloqueado

def print_labyrinth(lab):
    for row in lab:
        for column in row:
            print(column, end=" ")
        print()

def a_star_search(start: Cell, dst: Cell):
    # validaciones
    if not is_valid(start.row, start.column):
        print("Start cell is invalid")
        return []
        
    if not is_valid(dst.row, dst.column):
        print("Destionation cell is invalid")
        return []
    
    if is_blocked(start.row, start.column) or is_blocked(dst.row, dst.column):
        print("Start or destionation cell are blocked!")
        return []
    
    if is_destination(start.row, start.column, dst):
        print("We are in goal cell")
        return start.get_path()
    
    open_list = deque() # lista doblemente ligada, su usará como cola (FIFO) para almacenar las celdas

    # Matriz booleana para saber que celdas se han visitado
    # Se inicializa a False indicando que no se ha visitado ni uno
    closed_list = []
    for _ in range(ROWS):
        closed_list.append([False for _ in range(COLUMNS)])
    
    cell_details = []
    for row in range(ROWS):
        cell_details.append([Cell(position=(row, col)) for col in range(COLUMNS)])

    open_list.append(start) # agrega al final

    found_dst = False

    while len(open_list) != 0:
        current_cell = open_list.popleft() # elimina por la izquierda en O(1)
        row, column = current_cell.row, current_cell.column
        closed_list[row][column] = True

        f_new = g_new = h_new = 0
        # generacion de sucesores
        if is_valid(row-1, column):
            # generar arriba
            if is_destination(row-1, column, dst):
                cell_details[row-1][column].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row-1][column] == False and not is_blocked(row-1, column):
                g_new = cell_details[row][column].g + 1
                h_new = current_cell.manhattan_distance(dst)
                f_new = g_new + h_new

                if cell_details[row-1][column].f == 0 or cell_details[row-1][column].f > f_new:
                    open_list.append(Cell(position=(row-1, column), parent=current_cell))
                    successor_cell = cell_details[row-1][column]
                    successor_cell.f = f_new
                    successor_cell.g = g_new
                    successor_cell.h = h_new
                    successor_cell.parent = current_cell
    
        if is_valid(row, column+1):
            # genera derecha
            if is_destination(row, column+1, dst):
                cell_details[row][column+1].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row][column+1] == False and not is_blocked(row, column+1):
                g_new = cell_details[row][column].g + 1
                h_new = current_cell.manhattan_distance(dst)
                f_new = g_new + h_new

                if cell_details[row][column+1].f == 0 or cell_details[row][column+1].f > f_new:
                    open_list.append(Cell(position=(row, column+1), parent=current_cell))
                    cell_details[row][column+1].f = f_new
                    cell_details[row][column+1].g = g_new
                    cell_details[row][column+1].h = h_new
                    cell_details[row][column+1].parent = current_cell
    
        if is_valid(row+1, column):
            # genera abajo
            if is_destination(row+1, column, dst):
                cell_details[row+1][column].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row+1][column] == False and not is_blocked(row+1, column):
                g_new = cell_details[row][column].g + 1
                h_new = current_cell.manhattan_distance(dst)
                f_new = g_new + h_new

                if cell_details[row+1][column].f == 0 or cell_details[row+1][column].f > f_new:
                    open_list.append(Cell(position=(row+1, column), parent=current_cell))
                    cell_details[row+1][column].f = f_new
                    cell_details[row+1][column].g = g_new
                    cell_details[row+1][column].h = h_new
                    cell_details[row+1][column].parent = current_cell

        if is_valid(row, column-1):
            # genera izquierda
            if is_destination(row, column-1, dst):
                cell_details[row][column-1].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row][column-1] == False and not is_blocked(row, column-1):
                g_new = cell_details[row][column].g + 1
                h_new = current_cell.manhattan_distance(dst)
                f_new = g_new + h_new

                if cell_details[row][column-1].f == 0 or cell_details[row][column-1].f > f_new:
                    open_list.append(Cell(position=(row, column-1), parent=current_cell))
                    cell_details[row][column-1].f = f_new
                    cell_details[row][column-1].g = g_new
                    cell_details[row][column-1].h = h_new
                    cell_details[row][column-1].parent = current_cell

    # limpieza
    open_list.clear()
    closed_list.clear()
    cell_details.clear()
    
    if not found_dst:
        print("Failed to find path to destionation cell")
        return current_cell.get_path()
    
        
    return current_cell.get_path()

def greedy(start: Cell, dst: Cell):
    # validaciones
    if not is_valid(start.row, start.column):
        print("Start cell is invalid")
        return []

    if not is_valid(dst.row, dst.column):
        print("Destionation cell is invalid")
        return []

    if is_blocked(start.row, start.column) or is_blocked(dst.row, dst.column):
        print("Start or destionation cell are blocked!")
        return []

    if is_destination(start.row, start.column, dst):
        print("We are in goal cell")
        return start.get_path()

    # lista doblemente ligada, su usará como cola (FIFO) para almacenar las celdas
    open_list = deque()

    # Matriz booleana para saber que celdas se han visitado
    # Se inicializa a False indicando que no se ha visitado ni uno
    closed_list = []
    for _ in range(ROWS):
        closed_list.append([False for _ in range(COLUMNS)])

    cell_details = []
    for row in range(ROWS):
        cell_details.append([Cell(position=(row, col))
                            for col in range(COLUMNS)])

    open_list.append(start)  # agrega al final

    found_dst = False

    while len(open_list) != 0:
        current_cell = open_list.popleft()  # elimina por la izquierda en O(1)
        row, column = current_cell.row, current_cell.column
        closed_list[row][column] = True

        h_new = 0
        # generacion de sucesores
        if is_valid(row-1, column):
            # generar arriba
            if is_destination(row-1, column, dst):
                cell_details[row-1][column].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row-1][column] == False and not is_blocked(row-1, column):
                h_new = current_cell.manhattan_distance(dst)

                if cell_details[row-1][column].h == 0 or cell_details[row-1][column].h > h_new:
                    open_list.append(
                        Cell(position=(row-1, column), parent=current_cell))
                    successor_cell = cell_details[row-1][column]
                    successor_cell.h = h_new
                    successor_cell.parent = current_cell

        if is_valid(row, column+1):
            # genera derecha
            if is_destination(row, column+1, dst):
                cell_details[row][column+1].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row][column+1] == False and not is_blocked(row, column+1):
                h_new = current_cell.manhattan_distance(dst)

                if cell_details[row][column+1].h == 0 or cell_details[row][column+1].h > h_new:
                    open_list.append(
                        Cell(position=(row, column+1), parent=current_cell))
                    cell_details[row][column+1].h = h_new
                    cell_details[row][column+1].parent = current_cell

        if is_valid(row+1, column):
            # genera abajo
            if is_destination(row+1, column, dst):
                cell_details[row+1][column].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row+1][column] == False and not is_blocked(row+1, column):
                h_new = current_cell.manhattan_distance(dst)

                if cell_details[row+1][column].h == 0 or cell_details[row+1][column].h > h_new:
                    open_list.append(
                        Cell(position=(row+1, column), parent=current_cell))
                    cell_details[row+1][column].h = h_new
                    cell_details[row+1][column].parent = current_cell

        if is_valid(row, column-1):
            # genera izquierda
            if is_destination(row, column-1, dst):
                cell_details[row][column-1].parent = current_cell
                print("We are at destination")
                found_dst = True
                break
            elif closed_list[row][column-1] == False and not is_blocked(row, column-1):
                h_new = current_cell.manhattan_distance(dst)

                if cell_details[row][column-1].h == 0 or cell_details[row][column-1].h > h_new:
                    open_list.append(
                        Cell(position=(row, column-1), parent=current_cell))
                    cell_details[row][column-1].h = h_new
                    cell_details[row][column-1].parent = current_cell

    # limpieza
    open_list.clear()
    closed_list.clear()
    cell_details.clear()

    if not found_dst:
        print("Failed to find path to destionation cell")
        return current_cell.get_path()

    return current_cell.get_path()

def is_destination(row: int, column: int, goal: Cell):
    return row == goal.row and column == goal.column

def is_valid(row: int, column: int):
    return (row >= 0 and row < ROWS) and (column >= 0 and column < COLUMNS)

def is_blocked(row: int, column: int):
    return thick_labyrinth[row][column] == B
