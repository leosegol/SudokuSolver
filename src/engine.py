import numpy
import graphics

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

made = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def create_made():
    global made, grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                made[i][j] = False
            else:
                made[i][j] = True


def can_enter(x, y, n):
    global grid
    for x1 in range(9):
        if n == grid[y][x1]:
            return False
    for y1 in range(9):
        if n == grid[y1][x]:
            return False
    x1 = (x//3)*3
    y1 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y1+i][x1+j] == n:
                return False
    return True


def solve(w):
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if can_enter(x, y, n):
                        grid[y][x] = n
                        solve(w)
                        grid[y][x] = 0
                return
    print(grid)
    graphics.print_board(w, grid)
