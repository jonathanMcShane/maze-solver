from graphics import Window
from cell import Cell

def main():
    win = Window(1000, 1000)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(50, 50, 200, 200)

    win.wait_for_close()

main()